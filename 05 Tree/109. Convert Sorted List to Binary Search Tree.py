# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # (0) edge case
        if not head: 
            return None
        
        # (1) convert linked list into array
        treelist = []
        while head:
            treelist.append(TreeNode(head.val))
            head = head.next
            
        # (2) call the function like in the Problem 108
        return self.helper(treelist)

    def helper(self, treelist):
        if len(treelist) == 0:
            return None

        mid = len(treelist) // 2
        root = treelist[mid]
        root.left = self.helper(treelist[:mid])
        root.right = self.helper(treelist[mid+1:])
        return root
    
# Time: O(N) since we convert the linked list to an array initially and then we convert the array into a BST. Accessing the middle element in the array takes O(1) time.
# Space: O(N) since the array we construct initially.


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # (0) edge case
        if head is None:
            return None
        
        # (1) two pointers to find mid
        dummy = ListNode(0)              # (1.1) create a dummy node and connect it
        dummy.next = head
        curr = dummy

        fast = curr                      # (1.2) intialize the fast and slow pointers
        slow = curr
        left_tail = curr

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            left_tail = slow             # (1.3) left_tail is slower thant slow pointer
            slow = slow.next
        
        # (2) disconnect the left, mid, right
        left_tail.next = None
        root = TreeNode(slow.val)
        
        # (3) recursively call left and right
        root.left = self.sortedListToBST(dummy.next)
        root.right = self.sortedListToBST(slow.next)
        
        # (4) return root
        return root
    
    
# Time: O(NlogN) since we still have to process each of the nodes in the linked list once and form corresponding BST nodes.
# Space: O(logN) there is always the added space complexity of the recursion stack and since we are building a height balanced BST, the height is bounded by logN.