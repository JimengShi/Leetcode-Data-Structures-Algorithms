# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
       
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # (0) edge case
        if not head or k == 1:
            return head
        
        # (1) dummy node and connect it with head of linked list
        dummy = ListNode(-1)
        dummy.next = head
        
        # (2) length of linked list
        num = 0
        while head:
            head = head.next
            num += 1
        
        # (3) reverse
        pre = dummy
        while num >= k:
            cur = pre.next
            nxt = cur.next
            for _ in range(k-1):
                cur.next = nxt.next
                nxt.next = pre.next
                pre.next = nxt
                nxt = cur.next
            pre = cur
            num -= k
            
        # (4) return the final result
        return dummy.next  

    
# Time: O(N)
# Space: O(1)