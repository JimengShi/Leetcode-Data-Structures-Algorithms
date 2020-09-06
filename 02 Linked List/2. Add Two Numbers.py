# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # (1) create a dummy node for our output linked list
        dummy = ListNode(0)
        curr = dummy
        
        # (2) addition operation
        tempsum = 0
        while l1 or l2 or tempsum:         # while l1 or l2 or tempsum
            if l1:
                tempsum += l1.val
                l1 = l1.next
            if l2:
                tempsum += l2.val
                l2 = l2.next
            
            curr.next = ListNode(tempsum % 10)
            curr = curr.next
            tempsum = tempsum // 10
        
        # (3) return output
        return dummy.next

# Time: O(max(m,n)), m and n are the length of two linked lists
# Space: O(max(m,n))

# What if the the digits in the linked list are stored in non-reversed order? For example:
# (3→4→2)+(4→6→5)=8→0→7