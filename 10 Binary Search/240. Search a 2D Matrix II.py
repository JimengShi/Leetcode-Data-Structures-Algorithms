# Method 1: binary search each row
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


# Method 2: traverse along edge
class Solution:
    def searchMatrix(self, matrix, target):
        # (0) edge case
        m = len(matrix)
        if m < 1:
            return False
        n = len(matrix[0])
        if n < 1:
            return False
        
        # (1) traverse along edge
        row, col = 0, n - 1
        while row < m and col >= 0:
            curr = matrix[row][col]
            if target > curr:
                row += 1
            elif target < curr:
                col -= 1
            else:
                return True
            
        # (2) otherwise return False 
        return False
    
# Time: O(m+n)
# Space: O(1)