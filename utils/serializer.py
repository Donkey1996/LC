from turtle import left
from yaml import serialize
from .TreeNode import TreeNode
from collections import deque


class Serializer:
    def __init__(self):
        pass

    def serialize(self, root: TreeNode) -> str:
        if root is None:
            return ""
        res = ""
        q = deque([root])
        while q:
            cur = q.popleft()
            if cur is None:
                res += ",null"
            else:
                res += "," + str(cur.val)
                q.append(cur.left)
                q.append(cur.right)
        return res[1:]

    def deserialize(self, data: str) -> TreeNode:
        if data == "":
            return None
        nodes = [
            None if val == "null" else TreeNode(int(val))
            for val in data.strip("[]{}").split(",")
        ]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids:
                    node.left = kids.pop()
                if kids:
                    node.right = kids.pop()
        return root


def main():
    serializer = Serializer()
    root = serializer.deserialize(data="[1,2,3,null,null,4,null,null,5]")
    print(root.val)
    print(serializer.serialize(root))


if __name__ == "__main__":
    main()
