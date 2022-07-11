from typing import List, Optional
import pytest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_tree(vals: List[int]) -> TreeNode:
    if not List:
        return None
    
    n = len(vals)
    def _get_root(idx: int) -> TreeNode:
        if idx >= n or vals[idx] == None:
            return None
        root = TreeNode(vals[idx])
        root.left = _get_root(2*idx+1)
        root.right = _get_root(2*idx+2)
        return root

    return _get_root(0)

def test_tree_node():
    node_left = TreeNode(val=8, left=None, right=None)
    node_right = TreeNode(val=1818, left=None, right=None)
    root = TreeNode(val=8, left=node_left, right=node_right)
    assert root.left.val == 8
    assert root.right.val == 1818

def test_tree():
    vals = [1,2,3,None,5,None,4]
    root = list_to_tree(vals)
    assert root.left.val == 2
    assert root.right.val == 3
    assert root.left.left is None
    assert root.right.left is None
    assert root.left.right.val == 5
    assert root.right.right.val == 4


def main():
    pytest.main(['-q', 'TreeNode.py'])

if __name__ == "__main__":
    main()
