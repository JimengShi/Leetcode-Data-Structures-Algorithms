# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # (0) edge case
        if not head or not head.next:
            return head

        # (1) initialize dummy and curr
        dummy = ListNode(1)
        dummy.next = head
        curr = head

        # (2) traverse
        while curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        # (3) return result
        return dummy.next

# Time: O(N)
# Space: O(1)
