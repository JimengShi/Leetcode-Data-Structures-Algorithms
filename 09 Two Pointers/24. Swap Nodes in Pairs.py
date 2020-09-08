# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        # (0) edge case
        if not head:
            return
        
        # (1) create a dummy node and assign it as curr and connect curr with head
        dummy = ListNode(0)
        curr = dummy
        curr.next = head

        # (2) traverse the whole list and swap each pair
        while curr.next and curr.next.next:
            p1 = curr.next
            p2 = curr.next.next
            curr.next = p2          # connect cur and cur.next, pay attention to the order here
            p1.next = p2.next       # connect p1 and p1.next, pay attention to the order here
            p2.next = p1            # connect p2 and p2.next, pay attention to the order here
            
            curr = curr.next.next   # update the current node
            
        # (3) return the whole reformed list
        return dummy.next
    

# Time: O(N) where N is the size of the linked list.
# Space: O(1).