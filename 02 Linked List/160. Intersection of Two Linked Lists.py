# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:    
        if headA and headB:
            A, B = headA, headB
            while A != B:
                # A runs until ending point, then run at the starting point of B
                if A:             
                    A = A.next
                else:
                    A = headB
                # B runs until ending point, then run at the starting point of A    
                if B:
                    B = B.next
                else:
                    B = headA
            return A
        
        return None
    
# Time: O(m+n)
# Space: O(m+n)