# Given a linked list, rotate the list to the right by k places, where k is non-negative.

# Example 1:
# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL

# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL

# Example 2:
# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL

# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # (0) edge cases
        if not head or not head.next:
            return head
        
        # (1) close the linked list into the ring
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        old_tail.next = head
        
        # (2) find new tail: (n - k % n - 1)th node and new head: (n - k % n)th node
        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        
        # (3) break the ring
        new_tail.next = None
        
        # (4) return the result
        return new_head
    

# Time: O(N)
# Space: O(1)