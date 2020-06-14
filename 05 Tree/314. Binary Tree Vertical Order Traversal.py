# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Method 1: BFS with sorting
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        # (0) edge case
        if root is None:
            return []
        
        # (1) BFS traversal
        columnTable = defaultdict(list)
        queue = deque([(root, 0, 0)])
        while queue:
            node, row, column = queue.popleft()
            if node:
                columnTable[column].append(node.val)
                if node.left:
                    queue.append((node.left, row+1, column-1))
                if node.right:
                    queue.append((node.right, row+1, column+1))

        # (2) extract the values from the columnTable
        # (2) for each column, first sort by 'row', then by 'value', in ascending order
        res = []
        for col in sorted(columnTable.keys()):
            res.append(columnTable[col])
        return res

# Time: O(NlogN)
# Space: O(N)


# Method 2: BFS without sorting
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        # (0) edge case
        if root is None:
            return []
        
        # (1) BFS traversal
        columnTable = defaultdict(list)
        min_column = max_column = 0
        queue = deque([(root, 0, 0)])
        while queue:
            node, row, column = queue.popleft()
            if node:
                columnTable[column].append(node.val)
                min_column = min(min_column, column)
                max_column = max(max_column, column)
                if node.left:
                    queue.append((node.left, row+1, column-1))
                if node.right:
                    queue.append((node.right, row+1, column+1))

        # (2) extract the values from the columnTable
        # (2) for each column, first sort by 'row', then by 'value', in ascending order
        res = []
        for col in range(min_column, max_column+1):
            res.append(columnTable[col])
        return res

# Time: O(N)
# Space: O(N)