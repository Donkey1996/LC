from node import ListNode, list_to_list_nodes
from typing import Optional

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        list_nodes = []
        while head:
            list_nodes.append(head.val)
            head = head.next
        res = list_nodes[:left-1] + list_nodes[left-1: right][::-1] + list_nodes[right:]
        print(res)
        return list_to_list_nodes(res)

def main():
    tests = [
        {
            "vals": [1, 2, 3, 4, 5], 
            'left': 2,
            'right': 4,
            "result": list_to_list_nodes([1, 4, 3, 2, 5])
        }
    ]
    i = 0
    for test in tests:
        i += 1
        vals = test["vals"]
        root = list_to_list_nodes(vals)
        solver = Solution()
        print(solver.reverseBetween(root, test['left'], test['right']))
        assert solver.reverseBetween(root, test['left'], test['right']).val == test["result"].val
        print(f"Passed test case {i}")


if __name__ == "__main__":
    main()
