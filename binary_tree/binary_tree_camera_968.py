"""
968. Binary Tree Cameras
Hard

You are given the root of a binary tree. 
We install cameras on the tree nodes where each camera at a node can monitor its parent, 
itself, and its immediate children.

Return the minimum number of cameras needed to monitor all nodes of the tree.
"""


class Solution:
    def minCameraCover(self, root):
        return min(self.solve(root)[1:])

    def solve(self, root):
        if root is None:
            return 0, 0, float("inf")
        L = self.solve(root.left)
        R = self.solve(root.right)
        dp0 = L[1] + R[1]
        dp1 = min(L[2] + min(R[1:]), R[2] + min(L[1:]))
        dp2 = 1 + min(L) + min(R)
        return dp0, dp1, dp2
