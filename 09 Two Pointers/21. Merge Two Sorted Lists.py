# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Method 1: recursively
# Time: O(n+m) for traversing every node in two lists. m and n are the lengths of two list
# Space: O(n+m) for save all nodes.
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # (0) edge case  
        if not l1 or not l2:
            return l1 or l2
        
        # (1) recursively connect
        # (1.1) l1.val < l2.val
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        
        # (1.2) l1.val >= l2.val
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        
        
# Method 2: iteratively with two pointers
# Time: O(n+m). Because exactly one of l1 and l2 is incremented on each loop iteration, the while loop runs for a number of iterations equal to the sum of the lengths (m + n) of the two lists. All other work is constant, so the overall complexity is linear.
# Space: O(1). only allocates a few pointers, so it has a constant overall memory footprint.
class Solution(object):
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # (0) edge case
        if not l1 or not l2:
            return l1 or l2
        
        # (1) edge case
        dummy = ListNode(0)
        curr = dummy
        
        # (2) traverse l1 and l2 to connect the l1 and l2 with the length(min(l1, l2))
        while l1 and l2:
            if l1.val < l2.val:     
                curr.next = l1      # (2.1) connect current node with the node who is smaller
                l1 = l1.next        # (2.2) update l1 to be next after l1 has been connected
            else:
                curr.next = l2
                l2 = l2.next
                
            curr = curr.next        # (2.3) updata current node(move current node ahead one step)
        
        # (3) connect current node with l1 or l2 whose left node is not empty
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        
        # (4) return the new linked list after dummy node
        return dummy.next