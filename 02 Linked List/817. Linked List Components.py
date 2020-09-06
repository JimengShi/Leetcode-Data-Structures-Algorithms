# We are given head, the head node of a linked list containing unique integer values.

# We are also given the list G, a subset of the values in the linked list.

# Return the number of connected components in G, where two values are connected if they appear consecutively in the linked list.

# Example 1:
# Input: 
# head: 0->1->2->3
# G = [0, 1, 3]
# Output: 2

# Explanation: 
# 0 and 1 are connected, so [0, 1] and [3] are the two connected components.

# Example 2:
# Input: 
# head: 0->1->2->3->4
# G = [0, 3, 1, 4]
# Output: 2

# Explanation: 
# 0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:

        Gset = set(G)
        cur = head
        ans = 0
        
        while cur:
            if cur.val in Gset and getattr(cur.next, 'val', None) not in Gset:
                ans += 1
            cur = cur.next

        return ans
    
# Time: O(N+G.length), where N is the length of the linked list with root node head.
# Space: O(G.length), to store Gset.