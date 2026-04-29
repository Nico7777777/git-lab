from tree import Tree
from node import Node
import unittest
from contextlib import contextmanager
from io import StringIO
import sys

tree = Tree()


tree.add(4)
tree.add(3)
tree.add(8)
tree.add(0)
tree.add(2)

@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class TestMarks(unittest.TestCase):
    # @contextmanager
    def test_pre_order(self) -> None:
        with captured_output() as (out, _):
            tree._printPreorderTree(tree.root)
        # This can go inside or outside the `with` block
        output = out.getvalue().strip()
        print()
        self.assertEqual(output, '4 3 0 2 8')
        # return output
        
    # @contextmanager
    def test_post_order(self) -> None:
        with captured_output() as (out, _):
            tree._printPostorderTree(tree.root)
        output = out.getvalue().strip()
        print()
        self.assertEqual(output, '2 0 3 8 4')
        # return output

    def test_find_1(self) -> None:
        ret = tree._find(0, tree.root)
        assert ret.data == 0
    
    def test_find_2(self) -> None:
        ret = tree._find(10, tree.root)
        assert ret is None

if __name__ == '__main__':
    print("print normal (in order):")
    tree.printTree()
    unittest.main()