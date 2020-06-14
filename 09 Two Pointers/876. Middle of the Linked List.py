# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Method 1: Output to Array
class Solution(object):
    def middleNode(self, head):
        A = [head]
        while A[-1].next:
            A.append(A[-1].next)
        return A[len(A) / 2]
    
# Time: O(n)
# Space: O(n)


# Method 2: Two pointers
class Solution(object):
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
# Time: O(n)
# Space: O(1), the space is only used by slow and fast pointer.