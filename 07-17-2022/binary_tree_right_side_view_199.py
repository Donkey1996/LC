from typing import List, Optional
import sys
sys.path.insert(0, '/home/jerrymengxiao/dev/LC')

from utils.TreeNode import (
    TreeNode,
    list_to_tree
)

"""
Recursion with list comprehension
 1
/  \
2  3
/
4
[len(right):] skips node 2 (which is blocked by node 3), and saves only node 4 
(which you can see from the right side)
"""
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        right = self.rightSideView(root.right)
        left = self.rightSideView(root.left)
        return [root.val] + right + left[len(right):]

def main():
    tests = [
        {'vals': [1, 2, 3,4], 'rightSideView': [1, 3,4]},
        {'vals': [1,2,3,None,5,None,4], 'rightSideView': [1,3,4]}
    ]
    i=0
    for test in tests:
        i += 1
        vals = test['vals']
        root = list_to_tree(vals)
        solver = Solution()
        assert solver.rightSideView(root) == test['rightSideView']
        print(f'Passed test case {i}')

if __name__ == "__main__":
    main()
