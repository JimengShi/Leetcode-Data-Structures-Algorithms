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