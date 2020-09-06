# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Example:
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Method 1: min heap
from heapq import heappop, heappush
class Solution:
    def mergeKLists(self, lists):
        # (1) initialze a dummy node and current node and a heap
        heap = []
        dummy = ListNode(0)
        curr = dummy
        
        # (2) traverse all lists and put 1st number of k lists into heap (heap.size = k)
        for node in lists:
            if node:
                heappush(heap, (node.val, node))
                
        # (3) do some operations with heap
        while heap:
            # (3.1) connect current node with the node on the top of heap
            value, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            # (3.2) push the element that is next to the node you just removed into heap
            if curr.next:
                heapq.heappush(heap, (curr.next.val, curr.next))
                
        # (4) return the new linked list after dummu node
        return dummy.next
    
# Time: O(Nlogk) where k is the number of linked lists. N nodes in the final linked list.
# Space: O(N) for a new linked list. O(k) for heap


# Method 2: Divide and Conquer
class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None

        interval = 1
        while interval < len(lists):
            for i in range(0, len(lists)-interval, interval*2):
                lists[i] = self.merge2Lists(lists[i], lists[i+interval])
            interval *= 2
        return lists[0]

    def merge2Lists(self, l1, l2):
        dummy = curr = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
            
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
            
        return dummy.next
    
# Time: O(Nlogk) where k is the number of linked lists. N nodes in the final linked list.
# Space: O(1)