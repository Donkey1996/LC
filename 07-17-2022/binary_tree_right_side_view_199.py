from typing import List, Optional
import sys
sys.path.insert(0, '..')

from utils.TreeNode import (
    TreeNode,
    list_to_tree
)

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return 0

def main():
    vals = [1,2,3,None,5,None,4]
    print(list_to_tree(vals).right.val)

if __name__ == "__main__":
    main()
