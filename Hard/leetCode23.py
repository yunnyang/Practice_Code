# 23. Merge k Sorted Lists
#
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
#
# Example:
#
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        items = []
        for i in range(len(lists)):
            item = []
            if lists[i] != None:
                while lists[i].next != None:
                    item.append(lists[i].val)
                    lists[i] = lists[i].next

                item.append(lists[i].val)

                items.extend(item)

        items.sort()

        return self.makeListNode(items)

    def makeListNode(self, val: list()) -> ListNode:
        if len(val) == 0:
            return ListNode("")

        Head = ListNode(val[0])
        Result = Head

        for i in range(1, len(val)):
            Tail = ListNode(val[i])
            Head.next = Tail
            Head = Head.next

        return Result