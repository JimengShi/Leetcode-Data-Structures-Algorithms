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


# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         curA, curB = headA, headB
#         lenA, lenB = 0, 0
#         while curA is not None:         # find len(A)
#             lenA += 1
#             curA = curA.next
#         while curB is not None:         # find len(B)
#             lenB += 1
#             curB = curB.next
            
#         curA, curB = headA, headB
#         if lenA > lenB:                 # A runs len(A)-len(B) steps first
#             for i in range(lenA-lenB):
#                 curA = curA.next
#         elif lenB > lenA:
#             for i in range(lenB-lenA):  # B runs len(B)-len(A) steps first
#                 curB = curB.next
                
#         while curB != curA:
#             curB = curB.next
#             curA = curA.next
#         return curA 
    
# Time: O(m+n)
# Space: O(m+n)