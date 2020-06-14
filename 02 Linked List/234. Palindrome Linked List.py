# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Method 1:
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        fast = slow = head
        
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        # reverse the second half
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        
        # compare the first and second half nodes # while node and head:
        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
            
        return True
    
# Time: O(N)
# Space: O(1)


# Method 2:
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        nums = []
        
        while head:
            nums.append(head.val)
            head = head.next
        
        return nums == nums[::-1]
    
# Time: O(N)
# Space: O(N)