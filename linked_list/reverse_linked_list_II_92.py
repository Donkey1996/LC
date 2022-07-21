from node import ListNode, list_to_list_nodes
from typing import Optional

"""
92. Reverse Linked List II
Medium

Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, and return the reversed list.
"""


class Solution:
    # def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    #     """
    #     this solution uses a helper that first converts the root to a list of nodes
    #     do the reverse then converts it back to root;
    #     not ideal
    #     """
    #     list_nodes = []
    #     while head:
    #         list_nodes.append(head.val)
    #         head = head.next
    #     res = list_nodes[:left-1] + list_nodes[left-1: right][::-1] + list_nodes[right:]
    #     print(res)
    #     return list_to_list_nodes(res)

    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        """
        this solution uses a dummy node in front of the head
        then use the linked list operation only to reverse the desired chunk 
        学
        """
        if not head or left == right:
            return head
        p = dummy = ListNode(None)
        dummy.next = head
        for i in range(left - 1):
            p = p.next
        tail = p.next

        for i in range(right - left):
            tmp = p.next  # a)
            p.next = tail.next  # b)
            tail.next = tail.next.next  # c)
            p.next.next = tmp  # d)
        return dummy.next


def main():
    tests = [
        {
            "vals": [1, 2, 3, 4, 5],
            "left": 2,
            "right": 4,
            "result": list_to_list_nodes([1, 4, 3, 2, 5]),
        }
    ]
    i = 0
    for test in tests:
        i += 1
        vals = test["vals"]
        root = list_to_list_nodes(vals)
        solver = Solution()
        print(solver.reverseBetween(root, test["left"], test["right"]))
        assert (
            solver.reverseBetween(root, test["left"], test["right"]).val
            == test["result"].val
        )
        print(f"Passed test case {i}")


if __name__ == "__main__":
    main()
