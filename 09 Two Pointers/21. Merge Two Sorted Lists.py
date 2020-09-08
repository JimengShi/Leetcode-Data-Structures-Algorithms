# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Method 1: iteratively with two pointers
class Solution(object):
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # (0) edge case
        if not l1:
            return l2
        if not l2:
            return l1
        
        # (1) initialize a dummy node
        dummy = ListNode(0)
        curr = dummy
        
        # (2) traverse l1 and l2 to connect the l1 and l2 with the length(min(l1, l2))
        while l1 and l2:
            if l1.val < l2.val:     
                curr.next = l1     # (2.1) connect current node with node who is smaller
                l1 = l1.next       # (2.2) update l1 to be next after l1 was connected
            else:
                curr.next = l2
                l2 = l2.next
                
            curr = curr.next       # (2.3) updata curr node(move curr node ahead one step)
        
        # (3) connect current node with l1 or l2 whose left node is not empty
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        
        # (4) return the new linked list after dummy node
        return dummy.next

# Time: O(n+m).
# Space: O(1).


# Method 2: recursively
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
        
# Time: O(n+m) for traversing every node in two lists. m and n are the lengths of two list
# Space: O(n+m) for save all nodes.