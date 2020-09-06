# Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle.

# Notice that the row index starts from 0.

# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]

# Example 2:
# Input: rowIndex = 0
# Output: [1]

# Example 3:
# Input: rowIndex = 1
# Output: [1,1]


class Solution:
    def getRow(self, rowIndex):
        # (0) initialize an empty list to save answer triangle
        triangle = []

        # (1) initialize the framework, compute and append the reasonable answer
        for row_num in range(rowIndex+1):
            
            # (1.1) initialze a frame with first and last row elements are always 1
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            # (1.2) triangle element = the elements above-and-to-the-left + above-and-to-the-right.
            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]
            
            # (1.3) append the reasonable answer
            triangle.append(row)

        # (2) return the final result
        return triangle[-1]
    
    
# rowIndex k
# k = 0           1
# k = 1         1   1
# k = 2       1   2   1
# k = 3     1   3   3   1       
# k = 4   1   4   6   4   1
#         0   1   2   3   4  <--- j index
    
# Time: O(k^2)
# Space: O(k^2) for keeping only the latest generated row