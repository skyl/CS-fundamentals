import random

try:
    import pydot
except ImportError:
    print "Hey, you don't have pydot so you can make pictures"


class BinSearchNode(object):

    def __init__(self, data=0, parent=None):
        self.left = None
        self.right = None
        self.data = data
        self.parent = parent
        if parent is not None:
            if parent < self:
                parent.right = self
            elif parent > self:
                parent.left = self

    def __eq__(self, other):
        if other is None:
            return False
        return self.data == other.data

    def __le__(self, other):
        if other is None:
            return False
        return self.data <= other.data

    def __ge__(self, other):
        if other is None:
            return False
        return self.data >= other.data

    def __lt__(self, other):
        if other is None:
            return False
        return self.data < other.data

    def __gt__(self, other):
        if other is None:
            return False
        return self.data > other.data

    @property
    def is_child(self):
        return self.parent is not None

    @property
    def is_left(self):
        return self.is_child and (self.data < self.parent.data)

    @property
    def is_right(self):
        return self.is_child and (self.data > self.parent.data)

    @property
    def is_leaf(self):
        return (self.left is None) and (self.right is None)

    @property
    def has_two_children(self):
        return bool(self.left and self.right)

    @property
    def has_one_child(self):
        return (not self.is_leaf) and (not self.has_two_children)


class BinSearchTree(object):

    def __init__(self, root=None):
        if root is None:
            self.root = BinSearchNode()
        elif isinstance(root, BinSearchNode):
            self.root = root
        else:
            self.root = BinSearchNode(root)

    def search_recursive(self, data, node=None):
        if node is None:
            node = self.root

        if data == node.data:
            return node

        if data < node.data:
            if node.left is not None:
                return self.search_recursive(data, node.left)

        if data > node.data:
            if node.right is not None:
                return self.search_recursive(data, node.right)

        return None

    def search_iterative(self, data):
        next_node = self.root

        while next_node is not None:

            if data == next_node.data:
                return next_node

            elif data < next_node.data:
                next_node = next_node.left

            else:
                next_node = next_node.right

        return None

    search = search_iterative

    def insert_recursive(self, data, node=None):
        if node is None:
            node = self.root

        if data < node.data:
            if node.left is None:
                return BinSearchNode(data, parent=node)
            return self.insert_recursive(data, node.left)

        elif data > node.data:
            if node.right is None:
                return BinSearchNode(data, parent=node)
            return self.insert_recursive(data, node.right)

    def insert_iterative(self, data):
        node = self.root

        while node is not None:
            if node.data == data:
                return

            elif data < node.data:
                if node.left is None:
                    return BinSearchNode(data, parent=node)
                else:
                    node = node.left

            elif data > node.data:
                if node.right is None:
                    return BinSearchNode(data, parent=node)
                else:
                    node = node.right

    insert = insert_iterative

    def insert_iterable(self, iterable):
        for i in iterable:
            self.insert(i)

    def insert_random(self, num=20, minn=-100, maxn=100):
        for i in range(num):
            self.insert(random.randint(minn, maxn))

    def delete(self, data=None, node=None):
        """
        Supply node or data to delete.
        If both are supplied, node is used and data is ignored.
        """
        node = self. _node_from_data_or_node(data, node)

        if node.is_leaf:
            if node.is_right:
                node.parent.right = None
            elif node.is_left:
                node.parent.left = None
            node.parent = None
            del node
            return

        if node.has_one_child:
            child = node.left or node.right
            if node.parent.right == node:
                node.parent.right = child
            elif node.parent.left == node:
                node.parent.left = child
            child.parent = node.parent
            del node
            return

        direction = random.choice(["right", "left"])
        choice = getattr(node, direction)
        if direction == "left":
            del_node = self.find_max(choice)
        if direction == "right":
            del_node = self.find_min(choice)
        node.data = del_node.data
        self.delete(node=del_node)

    def find_min_iterative(self, node):
        while node:
            candidate_node = node
            node = node.left
        return candidate_node

    def find_min_recursive(self, node):
        if not node.left:
            return node
        return self.find_min_recursive(node.left)

    find_min = find_min_iterative

    def find_max_iterative(self, node):
        while node:
            candidate_node = node
            node = node.right
        return candidate_node

    def find_max_recursive(self, node):
        if not node.right:
            return node
        return self.find_max_recursive(node.right)

    find_max = find_max_iterative

    def delete_subtree(self, data=None, node=None):
        """Delete all children of node"""
        node = self._node_from_data_or_node(data, node)
        if node is None:
            return
        self.delete_subtree(node=node.left)
        self.delete_subtree(node=node.right)
        if node.is_leaf:
            self.delete(node=node)

    def _node_from_data_or_node(self, data, node):
        if node:
            if data:
                print "data ignored, using node"
            return node

        if data is None:
            return None
            #raise ValueError("Supply either node or data")

        node = self.search(data)
        return node

    # pydot graphs
    def write_png(self, path="example.png"):
        graph = pydot.Dot(graph_type="digraph")
        node = self.root
        self.add_edges(graph, node)
        graph.write_png(path)

    def add_edges(self, graph, node):
        if node.left is not None:
            edge = pydot.Edge(str(node.data), str(node.left.data))
            graph.add_edge(edge)
            self.add_edges(graph, node.left)
        if node.right is not None:
            edge = pydot.Edge(str(node.data), str(node.right.data))
            graph.add_edge(edge)
            self.add_edges(graph, node.right)

