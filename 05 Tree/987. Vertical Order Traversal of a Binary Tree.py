# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Method 1: BFS with sorting all nodes
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        # step 1). construct the global node list, with the coordinates
        node_list = []
        queue = deque([(root, 0, 0)])
        while queue:
            node, row, column = queue.popleft()
            if node is not None:
                node_list.append((column, row, node.val))
                queue.append((node.left, row + 1, column - 1))
                queue.append((node.right, row + 1, column + 1))

        # step 2). sort the global node list, according to the coordinates
        node_list.sort()

        # step 3). retrieve the sorted results partitioned by the column index
        res = {}
        for column, row, value in node_list:
            if column in res:
                res[column].append(value)
            else:
                res[column] = [value]
        return res.values()
    
# Time: O(N) for BFS traversal, O(NlogN) for sorting
# Space: O(N)


# Method 2: BFS with sorting partition columns
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        # (0) edge case
        if root is None:
            return []
        
        # (1) BFS traversal
        columnTable = defaultdict(list)
        min_column = max_column = 0
        queue = deque([(root, 0, 0)])
        while queue:
            node, row, column = queue.popleft()
            if node is not None:
                columnTable[column].append((row, node.val))
                min_column = min(min_column, column)
                max_column = max(max_column, column)
                queue.append((node.left, row + 1, column - 1))
                queue.append((node.right, row + 1, column + 1))

        # (2) extract the values from the columnTable
        # (2) for each column, first sort by 'row', then by 'value', in ascending order
        res = []
        for col in range(min_column, max_column + 1):
            res.append([val for row, val in sorted(columnTable[col])])
        return res
    
# Time: O(N) for BFS traversal, O(K*(N/K)*log(N/k))=O(N*log(N/k)) for sort in step 2
# Space: O(N)