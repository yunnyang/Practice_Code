# 236. Lowest Common Ancestor of a Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = collections.defaultdict(list)
        treeSaver = dict()
        queue = collections.deque()

        parent[root.val].append(root.val)
        queue.append(root)

        while queue:
            head = queue.popleft();
            treeSaver[head.val] = head

            if head.left != None:
                parent[head.left.val].append(head.left.val)
                parent[head.left.val].extend(parent[head.val])
                queue.append(head.left)

            if head.right != None:
                parent[head.right.val].append(head.right.val)
                parent[head.right.val].extend(parent[head.val])
                queue.append(head.right)

        pParent = parent[p.val]
        qParent = parent[q.val]

        for pp in pParent:
            if pp in qParent:
                return treeSaver[pp]