from typing import Optional, List
from collections import deque
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_list_nodes(list_node: List[int]) -> Optional[ListNode]:
    if list_node == []:
        return None
    q = deque(list_node)
    root = ListNode(val=q.popleft())
    head = root
    while len(q) != 0:
        next = ListNode(val=q.popleft())
        head.next = next
        head = next
    return root

def main():
    node3 = ListNode(3, None)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    root = ListNode(0, node1)
    res = []
    head = root
    while head:
        res.append(head.val)
        head = head.next
    print(res)
    print(head)
    print(root.val)

    root = list_to_list_nodes([1,2,3,4,5,6,7,8,9,10,11,12,13,14])
    print(root.val)
    print(root.next.val)
    print(root.next.next.next.next.next.next.next.next.next.next.next.next.next.val)
if __name__ == "__main__":
    main()

