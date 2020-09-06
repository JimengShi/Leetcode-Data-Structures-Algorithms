# Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

# Example 1:
# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL

# Example 2:
# Input: 2->1->3->5->6->4->7->NULL
# Output: 2->3->6->7->1->5->4->NULL


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