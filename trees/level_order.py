"""
Level order traversal
Given a binary tree, return the level order traversal of its nodes'
values. (ie, from left to right, level by level).
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
     /\
    15 7
return its level order traversal as:
[
[3],
[9,20],
[15,7] ]
"""


class Tree:
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value


def level_order(root):
    queue = [root]
    while root and queue:
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)
        print(root.value)
        queue.pop()
        root = queue[0]


if __name__ == '__main__':
    node1 = Tree(None, None, 15)
    node2 = Tree(None, None, 7)
    node3 = Tree(node1, node2, 20)
    node4 = Tree(None, None, 9)
    root = Tree(node4, node3, 3)
    level_order(root)
