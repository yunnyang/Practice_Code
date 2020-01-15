#19. Remove Nth Node From End of List

# Given a linked list, remove the n-th node from the end of list and return its head.
#
# Example:
#
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes 1->2->3->5.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        val = []
        while True:
            if head.next == None:
                break
            val.append(head.val)
            head = head.next
        val.append(head.val)

        val.pop(~(n - 1))
        return self.makeNode(val)

    def makeNode(self, val: list()) -> ListNode:
        if len(val) == 0:
            return ListNode("")

        Head = ListNode(val[0])
        Result = Head
        for i in range(1, len(val)):
            Tail = ListNode(val[i])
            Head.next = Tail
            Head = Head.next

        return Result

