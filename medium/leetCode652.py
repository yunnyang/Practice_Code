# 652. Find Duplicate Subtrees


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        stack = collections.deque()
        visited = []
        dupleTree = []
        stack.append(root)

        while stack:
            target = stack.pop()
            visited.append(target)
            if target.right != None and target.right:
                stack.append(target.right)

            if target.left != None and target.left:
                stack.append(target.left)

        for i in range(len(visited)):
            for j in range(i + 1, len(visited)):
                if self.isSameTree(visited[i], visited[j]):
                    print(i, j)
                    dupleTree.append(visited[i])

        return dupleTree

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # p and q are both None
        if not p and not q:
            return True
        # one of p and q is None
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and \
               self.isSameTree(p.left, q.left)