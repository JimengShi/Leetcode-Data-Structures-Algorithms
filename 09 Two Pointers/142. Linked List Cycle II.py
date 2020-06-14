# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        # (0) edge case
        if head is None:
            return None
        
        # (1) initialize two pointers and try the first meet
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break

        # (2) a single linked list without circle
        if fast is None or fast.next is None:   
            return None
        
        # (3) try the second meet
        fast = head                             # set fast at the head node
        while fast != slow:
            fast = fast.next
            slow = slow.next

        # (4) return the node slow pointer is pointing to
        return slow
    
    
# Time: O(n)
# Space: O(1)

# Reference: https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/linked-list-cycle-ii-kuai-man-zhi-zhen-shuang-zhi-/