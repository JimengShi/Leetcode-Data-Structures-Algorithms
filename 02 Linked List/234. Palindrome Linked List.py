# Given a singly linked list, determine if it is a palindrome.

# Example 1:
# Input: 1->2
# Output: false

# Example 2:
# Input: 1->2->2->1
# Output: true

# Follow up:
# Could you do it in O(n) time and O(1) space?


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nums = []
        
        while head:
            nums.append(head.val)
            head = head.next
        
        return nums == nums[::-1]
    
# Time: O(N)
# Space: O(N)


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        mid = self.findMin(head)
        rhead = mid.next
        mid.next = None
        return self.compare(head, self.reverse(rhead))
    
    def findMin(self, head):
        if head is None or head.next is None:
            return head
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def reverse(self, head):
        pre = None
        while head:
            nxt = head.next
            head.next = pre
            pre = head
            head = nxt
        return pre
    
    def compare(self, head1, head2):
        while head2:
            if head2.val != head1.val:
                return False
            head2 = head2.next
            head1 = head1.next
        return True
    
# Time: O(N)
# Space: O(1)