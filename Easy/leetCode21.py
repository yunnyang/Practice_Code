# 21. Merge Two Sorted Lists
#
# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1 = []
        list2 = []
        if l1 != None:
            while l1.next != None:
                list1.append(l1.val)
                l1 = l1.next

            list1.append(l1.val)

        if l2 != None:
            while l2.next != None:
                list2.append(l2.val)
                l2 = l2.next

            list2.append(l2.val)

        list1.extend(list2)
        list1.sort()

        return self.makeListNode(list1)

    def makeListNode(self, List: list()) -> ListNode:

        if len(List) == 0:
            return ListNode("")

        Head = ListNode(List[0])
        Result = Head
        for i in range(1, len(List)):
            Tail = ListNode(List[i])
            Head.next = Tail
            Head = Head.next

        return Result