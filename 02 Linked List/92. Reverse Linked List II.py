# Reverse a linked list from position m to n. Do it in one-pass.

# Note: 1 ≤ m ≤ n ≤ length of list.

# Example:
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # (0) edge case
        if m == n:
            return head
        
        # (1) create a dummy node and connect it with head node
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        
        # (2) pre moves m-1 steps from dummy node to (m-1)th node
        for i in range(m-1):
            pre = pre.next

        # (3) reverse the [m, n] nodes
        res = None
        curr = pre.next
        for i in range(n-m+1):
            nxt = curr.next
            curr.next = res
            res = curr
            curr = nxt
        
        # (4) adjust the final connections by pre.next and pre.next.next
        pre.next.next = curr
        pre.next = res

        # (5) return the whole reformed list
        return dummy.next
    

# Time: O(N) since we process each of the nodes at most once 
# Space: O(1) in-place