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
            return
        
        # (1) initialize an empty node and assign head as current node
        result = None
        curr = head

        # (2) traverse the list
        while curr:
            nxt = curr.next          # (2.1) get next of current node first
            curr.next = result       # (2.2) link reverse            
            result = curr            # (2.3) update result by moving result to current
            curr = nxt               # (2.4) update curr by moving current to next

        # (3) return result
        return result
    
# Time: O(N)
# Space: O(1)


# Method 2: Recursively
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        pre = self.reverseList(head.next)       #  1 --> 2 --> 3 --> 4 --> 5 --> NULL
        head.next.next = head                   #  1 --> 2 <-- 3 <-- 4 <-- 5
        head.next = None                        # head
        return pre
    
# Time: O(n). Assume that n is the list's length, the time complexity is O(n).
# Space: O(n). The extra space comes from implicit stack space due to recursion. The recursion could go up to n levels deep.