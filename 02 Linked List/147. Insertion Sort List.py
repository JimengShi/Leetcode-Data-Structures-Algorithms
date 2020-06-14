# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Method: two pointers
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)      # pre is the sorted part when see a new node, start from dummy
        cur = head               # cur is the unsorted part
        
        while cur is not None:
            pre = dummy
            while pre.next is not None and pre.next.val < cur.val:
                pre = pre.next
                
            temp = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = temp
        
        return dummy.next
    
# Time: O(n^2)
# Space: O(1)