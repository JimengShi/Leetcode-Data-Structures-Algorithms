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
        for i in range(m - 1):
            pre = pre.next

        # (3) reverse the [m, n] nodes
        result = None
        current = pre.next
        for i in range(n - m + 1):
            nxt = current.next
            current.next = result
            
            result = current
            current = nxt
        
        # (4) adjust the final connections by pre.next and pre.next.next
        pre.next.next = current
        pre.next = result

        # (5) return the whole reformed list
        return dummy.next
    

# Time: O(N)
# Space: O(1)