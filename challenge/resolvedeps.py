"""
Given a list of packages that need to be built and the dependencies
for each package, determine a valid order in which to build the packages.
"""


def resolvedeps(depmap):
    """
    map is:
    {
        foo: [bar, baz],
        bar: [quxx],
        # maybe try to accept different forms of "no dependencies"
        # but, let's say we always have all deps in the keys
        # baz: [],
        # baz: None,
        quux: [baz]
    }
    return {baz, quux, bar, foo}

    Note: this solution is bad. O(2^n) maybe? See resolvetopo below.
    """
    final = []
    unsatisfied = depmap.copy()
    modules = depmap.keys()

    while any(unsatisfied.values()):

        # hack to find cycles
        lastunsatisfied = unsatisfied.copy()

        for k, v in unsatisfied.items():
            newdeps = []
            if v is None:
                continue
            for dep in v:
                if dep not in modules:
                    raise Exception('No module {}!'.format(v))
                if dep not in final:
                    newdeps.append(dep)
            # we have no more deps for k and we haven't added it to our list
            if (not newdeps) and (k not in final):
                final.append(k)
                unsatisfied[k] = None
            else:
                unsatisfied[k] = newdeps

        if lastunsatisfied == unsatisfied:
            raise Exception('Cycle found!')

    return final


def resolvetopo(depmap):
    final = []
    modules = depmap.keys()
    temp = set()
    permanent = set()

    for mod in modules:
        visit(mod, depmap, temp, permanent, final)

    return final


def visit(mod, depmap, temp, permanent, final):
    if mod not in depmap:
        raise Exception('No module {}!'.format(mod))
    if mod in temp:
        raise Exception('Cycle found for {}'.format(mod))
    if mod in permanent:
        return

    temp.add(mod)
    for dep in depmap[mod]:
        visit(dep, depmap, temp, permanent, final)

    permanent.add(mod)
    temp.remove(mod)
    final.append(mod)
