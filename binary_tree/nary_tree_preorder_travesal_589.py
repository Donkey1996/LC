from typing import Any, Callable, Dict, List, Optional, Tuple, Union


class Solution:
    """
    similar to 144 binary preorder traversal
    """

    def preorder(self, root) -> List[int]:
        res = []
        self._search(root, res)
        return res

    def _search(self, root, res):
        if root:
            res.append(root.val)
            for child in root.children:
                self._search(child, res)
