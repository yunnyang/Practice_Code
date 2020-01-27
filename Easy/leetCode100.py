# 100. Same Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        if p == None and q == None:
            return True

        if (p == None and q != None) or (p != None and q == None):
            return False

        pSeq = self.bfs(p)

        qSeq = self.bfs(q)

        print(pSeq)
        print(qSeq)

        if pSeq != qSeq:
            return False

        else:
            return True

    def bfs(self, head):
        queue = collections.deque()
        visited = []
        seq = []
        queue.append(head)
        seq.append(head.val)

        while queue:
            node = queue.popleft()
            visited.append(node)

            if node.left != None and node.left not in visited:
                queue.append(node.left)
                seq.append(node.left.val)

            if node.left == None and node.right != None:
                seq.append("null")

            if node.right != None and node.right not in visited:
                queue.append(node.right)
                seq.append(node.right.val)

            if node.right == None and node.left != None:
                seq.append("null")

        return seq