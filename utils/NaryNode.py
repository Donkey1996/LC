from typing import List, Optional


class NaryNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = [] if children is None else children


def main():
    """
        1
       /|\ 
      3 2 4
     /\
    5  6
    """
    node5 = NaryNode(5, [])
    node6 = NaryNode(6, [])
    node3 = NaryNode(3, [node5, node6])
    node2 = NaryNode(2, [])
    node4 = NaryNode(4, [])
    node1 = NaryNode(1, [node3, node2, node4])

    print(node1.children)
    print(node2.children)


if __name__ == "__main__":
    main()
