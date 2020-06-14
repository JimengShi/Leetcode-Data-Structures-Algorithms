# Definition for singly-linked list.
# class ListNode(object)
#     def __init__(self, x)
#         self.val = x
#         self.next = None

class Solution(object)
    def reorderList(self, head)
        # (0) edge case
        if not head
            return 
        
        # (1) find middle of linked list [Problem 876], in 1-2-3-4-5-6 find 4 
        slow = fast = head
        while fast and fast.next
            slow = slow.next
            fast = fast.next.next 
            
        # (2) reverse second part of the list [Problem 206]
        # (2) convert 1-2-3-4-5-6 into 1-2-3-4 and 6-5-4
        prev = None
        curr = slow
        while curr
            curr.next = prev
            prev = curr
            curr = curr.next

        # (3) merge two sorted linked lists [Problem 21]
        # (3) merge 1-2-3-4 and 6-5-4 into 1-6-2-5-3-4
        first = head
        second = prev
        while second.next
            first.next = second
            first = first.next
            second.next = first
            second = second.next
            

# Time O(N). There are three steps here. To identify the middle node takes O(N) time. To reverse the second part of the list, one needs N2 operations. The final step, to merge two lists, requires N2 operations as well.
# Space O(1), since we do not allocate any additional data structures.

            
            
            