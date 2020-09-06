# Given a binary tree, return the vertical order traversal of its nodes values.
# For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

# Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, 
# we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

# If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.
# Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Method 1: BFS with sorting all nodes
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        # (0) edge case
        if root is None:
            return []
        
        # (1) initialize
        columnTable = defaultdict(list)
        queue = deque([(root, 0, 0)])

        # (2) BFS traversal
        while queue:
            node, row, column = queue.popleft()
            if node:
                columnTable[column].append((row, node.val))
                if node.left:
                    queue.append((node.left, row+1, column-1))
                if node.right:
                    queue.append((node.right, row+1, column+1))

        # (3) extract the values from the columnTable
        # (3) for each column, first sort by 'row', then by 'value', in ascending order
        res = []
        for col in sorted(columnTable.keys()):
            res.append([val for row, val in sorted(columnTable[col])])
        return res

# Time: O(N) for BFS traversal, O(NlogN) for sorting
# Space: O(N)


# Method 2: BFS with sorting partition columns
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
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
            if node is not None:
                columnTable[column].append((row, node.val))
                min_column = min(min_column, column)
                max_column = max(max_column, column)
                queue.append((node.left, row + 1, column - 1))
                queue.append((node.right, row + 1, column + 1))

        # (3) extract the values from the columnTable
        # (3) for each column, first sort by 'row', then by 'value', in ascending order
        res = []
        for col in range(min_column, max_column + 1):
            res.append([val for row, val in sorted(columnTable[col])])
        return res
    
# Time: O(N) for BFS traversal, O(K*(N/K)*log(N/k))=O(N*log(N/k)) for sort in step 2
# Space: O(N)