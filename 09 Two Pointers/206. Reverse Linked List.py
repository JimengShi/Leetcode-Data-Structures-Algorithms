# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Method 1: Iteratively
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # (0) edge case
        if not head or not head.next:
            return head
        
        # (1) initialize an empty node and assign head as current node
        pre = None
        curr = head

        # (2) traverse the list
        while curr:
            nxt = curr.next          # (2.1) get next of current node first
            curr.next = pre          # (2.2) link reverse            
            pre = curr               # (2.3) update result by moving result to current
            curr = nxt               # (2.4) update curr by moving current to next

        # (3) return result
        return pre
    
# Time: O(N)
# Space: O(1)


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # (0) edge case
        if not head or not head.next:
            return head
        
        # (1) initialize an empty node and assign head as current node
        pre = None
        curr = head

        # (2) traverse the list
        while curr:
            curr.next, pre, curr = pre, curr, curr.next

        # (3) return result
        return pre
    
# Time: O(N)
# Space: O(1)