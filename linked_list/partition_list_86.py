from node import ListNode, list_to_list_nodes
from typing import List, Optional

"""
86. Partition List
Medium

Given the head of a linked list and a value x, partition it such that all nodes less than x 
come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
"""


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = tail1 = ListNode()
        dummy2 = tail2 = ListNode()
        while head:
            this = ListNode(head.val, None)
            if head.val < x:
                tail1.next = this
                tail1 = this
            else:
                tail2.next = this
                tail2 = this
            head = head.next
        tail1.next = dummy2.next
        return dummy1.next


def main():
    tests = [
        {
            "vals": [1, 4, 3, 2, 5, 2],
            "x": 3,
            "result": list_to_list_nodes([1, 2, 2, 4, 3, 5]),
        },
        {"vals": [2, 1], "x": 2, "result": list_to_list_nodes([1, 2]),},
    ]
    i = 0
    for test in tests:
        i += 1
        vals = test["vals"]
        root = list_to_list_nodes(vals)
        x = test["x"]
        solver = Solution()
        print(solver.partition(root, x))
        assert solver.partition(root, x).val == test["result"].val
        print(f"Passed test case {i}")


if __name__ == "__main__":
    main()
