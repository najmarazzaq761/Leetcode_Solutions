# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: 
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lesser = ListNode(0)
        greater_equal = ListNode(0)
        i = lesser
        j = greater_equal
        while head:
            if head.val < x:          
                i.next = head
                i = i.next
            else:
                j.next = head
                j = j.next
            head = head.next
        j.next = None
        i.next = greater_equal.next
        return lesser.next
