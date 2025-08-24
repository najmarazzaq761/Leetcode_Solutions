# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None
        return self.mergeSort(lists, 0, len(lists)-1 )

    def mergeSort(self, lists, left, right):
        if left == right:
            return lists[left]
        mid = (left+right)//2
        l1 = self.mergeSort(lists, left, mid)
        l2 = self.mergeSort(lists, mid+1, right)
        return self.mergeTwoSorts(l1,l2)

    def mergeTwoSorts(self, l1,l2):
        dummy = ListNode(0)
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 if l1 else l2
        return dummy.next           