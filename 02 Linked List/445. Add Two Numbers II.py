# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Method 1: with reversion
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # (1) reverse input linked list
        def reverseList(node):
            pre = None
            while node:
                nxt = node.next
                node.next = pre
                pre = node
                node = nxt
            return pre
        l1 = reverseList(l1)
        l2 = reverseList(l2)
        
        # (2) create a dummy node for output linked list
        dummy = ListNode(-1)
        cur = dummy
        tempsum = 0
        while l1 or l2 or tempsum:
            if l1:
                tempsum += l1.val
                l1 = l1.next
            if l2:
                tempsum += l2.val
                l2 = l2.next
            cur.next = ListNode(tempsum % 10)
            tempsum //= 10
            cur = cur.next
        
        # (3) return output linked list
        return reverseList(dummy.next)
    
# Time: O(max(m,n)), m and n are the length of two linked lists
# Space: O(max(m,n))


# Method 2: without reversion
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # (1) save l1 and l2 with stack
        s1 = []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        s2 = []
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        # (2) create a dummy node for output linked list
        head = None
        tempsum = 0
        while s1 or s2 or tempsum:
            if s1:
                tempsum += s1.pop()
            if s2:
                tempsum += s2.pop()
            node = ListNode(tempsum % 10)
            node.next = head
            head = node
            tempsum //= 10
        
        # (3) return output linked list
        return head
    
# Time: O(max(m,n)), m and n are the length of two linked lists
# Space: O(max(m,n))