# Given a binary tree, return the vertical order traversal of its nodes' values. 
# (ie, from top to bottom, column by column).
# If two nodes are in the same row and column, the order should be from left to right.

# Examples 1:
# Input: [3,9,20,null,null,15,7]
#    3
#   /\
#  /  \
#  9  20
#     /\
#    /  \
#   15   7 

# Output:
# [
#   [9],
#   [3,15],
#   [20],
#   [7]
# ]

# Examples 2:
# Input: [3,9,8,4,0,1,7]
#      3
#     /\
#    /  \
#    9   8
#   /\  /\
#  /  \/  \
#  4  01   7 

# Output:
# [
#   [4],
#   [9],
#   [3,0,1],
#   [8],
#   [7]
# ]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Method 1: BFS with sorting
from collections import defaultdict, deque
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        # (0) edge case
        if root is None:
            return []
        
        # (1) initialize
        columnTable = defaultdict(list)
        queue = deque([(root, 0, 0)])

        # (2) BFS traversal
        while queue:
            node, row, column = queue.popleft()
            columnTable[column].append(node.val)
            if node.left:
                queue.append((node.left, row+1, column-1))
            if node.right:
                queue.append((node.right, row+1, column+1))

        # (3) extract the values from the columnTable
        res = []
        for col in sorted(columnTable.keys()):
            res.append(columnTable[col])
        return res

# Time: O(NlogN)
# Space: O(N)


# Method 2: BFS without sorting
from collections import defaultdict, deque
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        # (0) edge case
        if root is None:
            return []
        
        # (1) initialize
        columnTable = defaultdict(list)
        min_column = max_column = 0
        queue = deque([(root, 0, 0)])

        # (2) BFS traversal
        while queue:
            node, row, column = queue.popleft()
            min_column = min(min_column, column)
            max_column = max(max_column, column)
            columnTable[column].append(node.val)
            if node.left:
                queue.append((node.left, row+1, column-1))
            if node.right:
                queue.append((node.right, row+1, column+1))

        # (3) extract the values from the columnTable
        res = []
        for col in range(min_column, max_column+1):
            res.append(columnTable[col])
        return res

# Time: O(N)
# Space: O(N)