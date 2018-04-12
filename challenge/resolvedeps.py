"""
Given a list of packages that need to be built and the dependencies
for each package, determine a valid order in which to build the packages.
"""


def resolvedeps(map):
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
    """
    final = []
    unsatisfied = map.copy()
    modules = map.keys()

    while any(unsatisfied.values()):

        for k, v in unsatisfied.items():
            newdeps = []
            for dep in v:
                if dep not in modules:
                    raise Exception('No module {}!'.format(v))
                if dep not in final:
                    newdeps.append(dep)
            # we have no more deps for k and we haven't added it to our list
            if (not newdeps) and (k not in final):
                final.append(k)
            else:
                unsatisfied[k] = newdeps

    return final
