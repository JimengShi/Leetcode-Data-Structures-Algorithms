# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Example: Given the sorted array: [-10,-3,0,5,9],
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#       0
#      / \
#    -3   9
#    /   /
#  -10  5


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:                                # (0) edge case
            return None

        mid = len(nums) // 2                              # (1) create mid node
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])     # (2) recursively to build left
        root.right = self.sortedArrayToBST(nums[mid+1:])  # (3) recursively to build right

        return root
    
# O(N) since each node will be exactly visited once
# O(N) to keep the output, O(logN) for the recursion stack