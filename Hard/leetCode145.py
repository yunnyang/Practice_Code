# 145. Binary Tree Postorder Traversal


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        traversal = []

        if root == None:
            return []

        return self.postorderHelper(root, traversal)

    def postorderHelper(self, root, part):
        if root.left != None:
            self.postorderHelper(root.left, part)
        if root.right != None:
            self.postorderHelper(root.right, part)

        part.append(root.val)

        return part