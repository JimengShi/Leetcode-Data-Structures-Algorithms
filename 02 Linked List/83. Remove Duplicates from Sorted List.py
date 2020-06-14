# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        node = head

        while node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next

        return head

# Time: O(N)
# Space: O(1)

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        node = head
        nxt = node.next
        while nxt:
            if node.val == nxt.val:
                node.next = nxt.next
                nxt = nxt.next
            else:
                node = nxt

        return head
    
# Time: O(N)
# Space: O(1)