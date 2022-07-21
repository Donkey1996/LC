"""
similar to 589
"""
from typing import List


class Solution:
    def postorder(self, root) -> List[int]:
        res = []
        self._search(root, res)
        return res

    def _search(self, root, res):
        if root:
            for child in root.children:
                self._search(child, res)
            res.append(root.val)
