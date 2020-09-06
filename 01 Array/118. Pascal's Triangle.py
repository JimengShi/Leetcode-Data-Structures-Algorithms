# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

# Example:

# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]


class Solution:
    def generate(self, num_rows):
        # (0) initialize an empty list to save answer triangle
        triangle = []

        # (1) initialize the framework, compute and append the reasonable answer
        for row_num in range(num_rows):
            
            # (1.1) initialze a frame with first and last row elements are always 1
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            # (1.2) triangle element = the elements above-and-to-the-left + above-and-to-the-right.
            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]
            
            # (1.3) append the reasonable answer
            triangle.append(row)

        # (2) return the final result
        return triangle
    
    
# Time: O(numRows^2), 1 + 2 + 3 + ... + (numRows-2) --> O(numRows^2)
# Space: O(numRows^2), since we need to store each number 1 + 2 + 3 + ... + numRows --> O(numRows^2)


# row_num   
#   1           [1]
#   2        [1,   1]
#   3     [1,  None,  1]
#   4   [1,  None, None, 1]
#       j-1  j+1
#   5 [1, None, None, None, 1]
#        j