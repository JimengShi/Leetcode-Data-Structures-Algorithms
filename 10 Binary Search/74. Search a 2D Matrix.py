# Method 1: brute force
class Solution:
    def searchMatrix(self, matrix, x):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == x:
                    return i, j
            
# Time: O(mn)
# Space: O(1)
            
            
# Method 2: binary search
class Solution:
    def searchMatrix(self, matrix, target):
        # (0) edge case
        m = len(matrix)
        if m < 1:
            return False
        n = len(matrix[0])
        if n < 1:
            return False
        
        # (1) start with the first row and run binary search in each row
        i = 0
        while i < m and target >= matrix[i][0]:
            low, high = 0, n-1
            while low <= high:
                mid = (low+high) // 2
                if target > matrix[i][mid]:
                    low = mid + 1
                elif target < matrix[i][mid]:
                    high = mid - 1
                else:
                    return True

            i += 1
        
        # (2) otherwise return False
        return False
    
# Time: O(mlogn)
# Space: O(1)


# Method 3: binary search, consider the matrix as a big array
# The first integer of each row is greater than the last integer of the previous row.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        
        # binary search
        left, right = 0, m * n - 1
        while left <= right:
                pivot_idx = (left + right) // 2
                pivot_element = matrix[pivot_idx // n][pivot_idx % n]
                if target == pivot_element:
                    return True
                else:
                    if target < pivot_element:
                        right = pivot_idx - 1
                    else:
                        left = pivot_idx + 1
        return False
    
# Time: O(logmn)
# Space: O(1)