# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

# Example:
# Given this linked list: 1->2->3->4->5
# For k = 2, you should return: 2->1->4->3->5
# For k = 3, you should return: 3->2->1->4->5

# Note:
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be changed.


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