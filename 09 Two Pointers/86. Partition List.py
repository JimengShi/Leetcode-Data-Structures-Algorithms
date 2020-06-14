# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        # (0) edge case
        if not head:
            return
        
        # (1) maintain before and after are the two pointers used to create two list
        before = before_head = ListNode(0)  # before_head are dummy node to save head of before list
        after = after_head = ListNode(0)    # before_head are dummy node to save head of after list

        # (2) start traversing the original list
        while head:
            if head.val < x:          # original list node < given x, assign it to before list
                before.next = head
                before = before.next
            else:
                after.next = head     # original list node >= the given x, assign it to after list
                after = after.next
            head = head.next          # move ahead in the original list

        # (3) connect last node of "after" with None in new reformed list and connect before and after
        after.next = None
        before.next = after_head.next

        # (4) return the whole new list
        return before_head.next
    
# Time: O(N), where N is the number of nodes in the original linked list.
# Space: O(1)