# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Method 1: linked and update pointer at the same time
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # (0) edge case
        if not head:
            return 
        
        # (1) find the mid of linked list [Problem 876], in 1->2->3->4->5->6 find 4 
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            
        # (2) reverse the second part of the list [Problem 206]
        # (2) convert 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4
        pre, curr = None, slow
        while curr:
            curr.next, pre, curr = pre, curr, curr.next       

        # (3) merge two sorted linked lists [Problem 21]
        # (3) merge 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4
        first, second = head, pre
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next

# Time: O(N)
# Space: O(1)       
    

# Method 2: linked first, and then update pointer
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # (0) edge case
        if not head:
            return 
        
        # (1) find the mid of linked list [Problem 876], in 1->2->3->4->5->6 find 4 
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            
        # (2) reverse the second part of the list [Problem 206]
        # (2) convert 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4
        pre = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt   

        # (3) merge two sorted linked lists [Problem 21]
        # (3) merge 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4    
        first = head
        second = pre
        while second.next:
            temp1 = first.next
            first.next = second
            first = temp1
            
            temp2 = second.next
            second.next = first
            second = temp2
            
# Time: O(N)
# Space: O(1)