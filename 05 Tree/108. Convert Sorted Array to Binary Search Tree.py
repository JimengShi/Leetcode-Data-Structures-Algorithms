# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# O(N) since each node will be exactly visited once
# O(N) to keep the output

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