# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        # get mid element to split two small links
        mid = self.getMiddle(head)   
        rHead = mid.next          # right list: after mid node
        mid.next = None           # left list: before mid node (include mid) and connect mid.next = None
        # sort two small links and then to merge them
        return self.merge(self.sortList(head), self.sortList(rHead))

    
    def getMiddle(self, head):
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    
    def merge(self, lHead, rHead):
        dummy = ListNode(0)
        curr = dummy
        while lHead and rHead:
            if lHead.val < rHead.val:
                curr.next = lHead
                lHead = lHead.next
            else:
                curr.next = rHead
                rHead = rHead.next
            curr = curr.next
            
        if lHead:
            curr.next = lHead
        elif rHead:
            curr.next = rHead
            
        return dummy.next
    
    
# Time: O(nlogn)
# Space: O(1)