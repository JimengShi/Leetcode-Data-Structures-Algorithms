# Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random

class Solution(object):
    def copyRandomList(self, head):
        # (0) edge case
        if head == None:
            return head
        
        # (1) initialize a dictionary
        dic = dict()
        
        # (2) 1st loop: copy all of orginal nodes, these nodes are separated, just have value without any pointer
        curr = head
        while curr:
            dic[curr] = Node(curr.val, None, None)
            curr = curr.next

        # (3) 2nd loop: connect next pointer and random pointer of these nodes
        curr = head
        while curr:
            dic[curr].next = dic.get(curr.next)       # set next pointer of dic[curr] node
            dic[curr].random = dic.get(curr.random)   # set random pointer of dic[curr] node
            curr = curr.next
            
        # (4) return result
        return dic.get(head)
    
# Time: O(N)
# Spacee: O(N)