# 86. Partition List
#
# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the two partitions.
#
# Example:
#
# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        nodesLeft = list()
        nodesRight = list()

        if head == None:
            return None

        while head != None:
            if head.val < x:
                nodesLeft.append(head.val)
                head = head.next
            else:
                nodesRight.append(head.val)
                head = head.next

        Left = self.makeList(nodesLeft)
        Right = self.makeList(nodesRight)

        if Left != None:
            Result = Left
        else:
            Result = Right

        while Left != None:
            if Left.next == None:
                Left.next = Right
                break
            Left = Left.next

        return Result

    def makeList(self, nodes: list) -> ListNode:
        if len(nodes) == 0:
            return None

        if len(nodes) == 1:
            return ListNode(nodes[0])

        Node = ListNode(nodes[0])
        Head = Node
        for i in range(1, len(nodes)):
            temp = ListNode(nodes[i])
            Node.next = temp
            Node = Node.next

        return Head