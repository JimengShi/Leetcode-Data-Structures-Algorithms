# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        
        while head and head.next:
            if head.val == head.next.val:
                # move head one step if head.val == head.next.val
                while head and head.next and head.val == head.next.val:  
                    head = head.next
                head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next
        return dummy.next

# Time: O(N)
# Space: (1)


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