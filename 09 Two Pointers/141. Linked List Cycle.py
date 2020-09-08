# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # (0) edge case
        if not head or not head.next:
            return False
        
        # (1) initialize two pointers
        slow = fast = head
        
        # (2) start traverse linked list
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:            # fast pointer can chase (meet) flow pointer
                return True
        
        # (3) otherwise return False
        return False

# 快慢双指针追赶碰撞解法
# Time: O(N)
# Space: O(1) is used by slow and fast pointers


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # (0) edge case
        if not head or not head.next:
            return False
        
        # (1) initialize two pointers
        slow = fast = head
        
        # (2) start traverse linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:            # fast pointer can chase (meet) flow pointer
                return True
        
        # (3) otherwise return False
        return False

# 快慢双指针追赶碰撞解法
# Time: O(N)
# Space: O(1) is used by slow and fast pointers