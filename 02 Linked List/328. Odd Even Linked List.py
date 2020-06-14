# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # (0) edge case
        if not head:
            return head
        
        # (1) create odds dummy and even dummy
        odds_dummy = ListNode(0)
        evens_dummy = ListNode(0)
        odds = odds_dummy
        evens = evens_dummy
        
        # (2) get odd index nodes and even index nodes
        isOdd = 1
        while head:
            if isOdd % 2 == 1:        # odd index
                odds.next = head
                odds = odds.next
            else:                     # even index
                evens.next = head
                evens = evens.next
            isOdd = isOdd + 1
            head = head.next
        
        # (3) connect odd node linked list and even node linked list
        evens.next = None
        odds.next = evens_dummy.next
        
        # (4) return result
        return odds_dummy.next
    
# Time: O(N). There are total nn nodes and we visit each node once.
# Space: O(1). All we need is the four pointers.