# 230. Kth Smallest Element in a BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if root == None:
            return 0

        stack = collections.deque()
        while True:
            if root:
                stack.append(root)
                root = root.left
            elif stack:
                root = stack.pop()

                k -= 1

                if k == 0:
                    return root.val
                root = root.right
            else:
                break
