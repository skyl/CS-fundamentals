import unittest2 as unittest
import mock

try:
    import pydot
except ImportError:
    pydot = None

from bst import BinSearchNode, BinSearchTree


class BinSearchNodeTests(unittest.TestCase):

    def setUp(self):
        self.parent = BinSearchNode()
        self.child_right = BinSearchNode(10, parent=self.parent)
        self.child_left = BinSearchNode(-10, parent=self.parent)

    def tearDown(self):
        pass

    def test_eq(self):
        self.assertEquals(self.parent, BinSearchNode())
        self.assertEquals(self.child_right, BinSearchNode(10))
        self.assertEquals(self.child_left, BinSearchNode(-10))
        self.assert_(not(self.child_right == None))

    def test_lt(self):
        self.assertTrue(self.parent < BinSearchNode(5))
        self.assertTrue(not (self.parent < None))

    def test_gt(self):
        self.assertTrue(self.parent > BinSearchNode(-5))
        self.assertTrue(not (self.parent > None))

    def test_le(self):
        self.assertTrue(self.parent <= BinSearchNode(5))
        self.assertTrue(not (self.parent <= None))

    def test_ge(self):
        self.assertTrue(self.parent >= BinSearchNode(-5))
        self.assertTrue(not (self.parent >= None))

    def test_is_child(self):
        self.assertTrue(self.child_right.is_child)
        self.assertTrue(self.child_left.is_child)
        self.assertTrue(not self.parent.is_child)

    def test_is_left(self):
        self.assertTrue(self.child_left.is_left)
        self.assertTrue(not self.child_right.is_left)
        self.assertTrue(not self.parent.is_left)

    def test_is_right(self):
        self.assertTrue(self.child_right.is_right)
        self.assertTrue(not self.child_left.is_right)
        self.assertTrue(not self.parent.is_right)

    def test_is_leaf(self):
        self.assertTrue(self.child_right.is_leaf)
        self.assertTrue(self.child_left.is_leaf)
        self.assertTrue(not self.parent.is_leaf)
        new_node = BinSearchNode(5, parent=self.child_right)
        self.assertTrue(not self.child_right.is_leaf)
        self.assertTrue(new_node.is_leaf)

    def test_has_two_children(self):
        nn1 = BinSearchNode(5, parent=self.child_right)
        nn2 = BinSearchNode(15, parent=self.child_right)
        self.assertTrue(self.child_right.has_two_children)
        self.assertTrue(self.parent.has_two_children)
        self.assertTrue(not self.child_left.has_two_children)
        self.assertTrue(not nn1.has_two_children)
        self.assertTrue(not nn2.has_two_children)

    def test_has_one_child(self):
        nn1 = BinSearchNode(5, parent=self.child_right)
        self.assertTrue(self.child_right.has_one_child)
        self.assertTrue(not self.parent.has_one_child)
        self.assertTrue(not self.child_left.has_one_child)
        self.assertTrue(not nn1.has_one_child)

    def test_parent_side_effects(self):
        self.assertEquals(self.parent.right, self.child_right)


class BinSearchTreeTests(unittest.TestCase):

    def setUp(self):
        normal_tree = [10, -10, -20, -5, -25, -15, -7, -3, 5, 3, 7, 20, 15, 25]
        self.bst = BinSearchTree()
        self.bst.insert_iterable(normal_tree)

    def tearDown(self):
        self.bst = None

    def test_init(self):
        bst = BinSearchTree()
        self.assertEqual(bst.root.data, 0)
        bst = BinSearchTree(root=BinSearchNode(100))
        self.assertEqual(bst.root.data, 100)
        bst = BinSearchTree(root=5)
        self.assertEqual(bst.root.data, 5)

    def test_search_recursive(self):
        n = self.bst.search_recursive(25)
        self.assertEqual(n.data, 25)
        n = self.bst.search_recursive(-25)
        self.assertEqual(n.data, -25)
        n = self.bst.search_recursive(420)
        self.assert_(n is None)

    def test_search_iterative(self):
        n = self.bst.search(15)
        self.assertEqual(n.data, 15)
        n = self.bst.search(-15)
        self.assertEqual(n.data, -15)
        n = self.bst.search(240)
        self.assert_(n is None)

    def test_insert_recursive(self):
        n = self.bst.insert_recursive(100)
        self.assertEqual(n.parent.data, 25)
        n = self.bst.insert_recursive(-100)
        self.assertEqual(n.parent.data, -25)

    def test_insert_iterative(self):
        n = self.bst.insert(0)
        self.assert_(n is None)
        n = self.bst.insert(100)
        self.assertEqual(n.parent.data, 25)
        n = self.bst.insert(-100)
        self.assertEqual(n.parent.data, -25)

    def test_insert_random(self):
        # TODO, hrm .. assert some stuff ..
        self.bst.insert_random()

    def test_delete_leaf(self):
        n = self.bst.search(20)
        self.assert_(n.has_two_children)
        self.bst.delete(25)
        self.assert_(n.has_one_child)
        self.assert_(n.right is None)

        n = self.bst.search(-20)
        self.assert_(n.has_two_children)
        self.bst.delete(-25)
        self.assert_(n.has_one_child)
        self.assert_(n.left is None)

    def test_delete_one_child_right(self):
        self.bst.insert(100)
        n = self.bst.search(25)
        self.assert_(n.has_one_child)
        self.bst.delete(25)
        n = self.bst.search(25)
        self.assert_(n is None)
        n = self.bst.search(100)
        self.assertEqual(n.parent.data, 20)

    def test_delete_one_child_left(self):
        self.bst.insert(-100)
        n = self.bst.search(-25)
        self.assert_(n.has_one_child)
        self.bst.delete(-25)
        n = self.bst.search(-25)
        self.assert_(n is None)
        n = self.bst.search(-100)
        self.assertEqual(n.parent.data, -20)

    @mock.patch("bst.random.choice")
    def test_delete_right_two_children(self, mock):
        mock.return_value = "right"
        self.bst.delete(10)
        n = self.bst.search(10)
        self.assert_(n is None)

        self.assertEqual(self.bst.root.right.data, 15)
        self.assertEqual(self.bst.root.right.right.data, 20)
        self.assertEqual(self.bst.root.right.right.right.data, 25)

        self.assertEqual(self.bst.root.right.left.data, 5)
        self.assertEqual(self.bst.root.right.left.right.data, 7)
        self.assertEqual(self.bst.root.right.left.left.data, 3)

    @mock.patch("bst.random.choice")
    def test_delete_left_two_children(self, mock):
        mock.return_value = "left"
        self.bst.delete(10)
        n = self.bst.search(10)
        self.assert_(n is None)
        self.assertEqual(self.bst.root.right.data, 7)
        self.assertEqual(self.bst.root.right.right.data, 20)
        self.assertEqual(self.bst.root.right.right.right.data, 25)
        self.assertEqual(self.bst.root.right.right.left.data, 15)
        self.assertEqual(self.bst.root.right.left.data, 5)
        self.assertEqual(self.bst.root.right.left.left.data, 3)

    def test_find_min_recursive(self):
        n = self.bst.find_min_recursive(self.bst.root)
        self.assertEqual(n.data, -25)

    def test_find_max_recursive(self):
        n = self.bst.find_max_recursive(self.bst.root)
        self.assertEqual(n.data, 25)

    def test_delete_subtree(self):
        self.bst.delete_subtree(10)
        self.assert_(self.bst.root.right is None)

    def test_node_from_data_or_node(self):
        node = self.bst._node_from_data_or_node(data=999, node=self.bst.root)
        self.assertEquals(node, self.bst.root)

    @unittest.skipIf(pydot is None, "there is no pydot in env")
    def test_pydot(self):
        self.bst.write_png(path="XXbarfoo.PNG")
        import os
        os.remove("XXbarfoo.PNG")


if __name__ == '__main__':
    unittest.main()

