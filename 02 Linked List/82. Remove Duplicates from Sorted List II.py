# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        pre = dummy
        dummy.next = head
        curr = head
        
        while curr and curr.next:
            if curr.val == curr.next.val:
                # move head one step if head.val == head.next.val
                while curr and curr.next and curr.val == curr.next.val:  
                    curr = curr.next
                curr = curr.next
                pre.next = curr
            else:
                pre = curr
                curr = curr.next
        return dummy.next

# Time: O(N)
# Space: O(1)


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        res = {}
        while head:
            if head.val not in res:
                res[head.val] = 1
            else:
                res[head.val] += 1
            head = head.next

        dummy = ListNode(0)
        curr = dummy 
        for key, val in res.items():
            if val == 1:
                new_node = ListNode(key)
                curr.next = new_node
                curr = new_node 
        return dummy.next

# Time: O(N)
# Space: (N)