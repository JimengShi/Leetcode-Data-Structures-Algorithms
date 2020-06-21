# Length of Longest Common Subsequence
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # (0) edge case
        if not text1 or not text2:
            return 0
        
        # (1) initialize a 2D DP array with all 0s
        matrix = [[0 for l in range(len(text1)+1)] for l in range(len(text2)+1)]
        
        # (2) fill 2D DP array, i and j are indice of DP array
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if text1[j-1] == text2[i-1]:               # (2.1) ith char and jth char is same
                    matrix[i][j] = matrix[i-1][j-1] + 1
                else:                                      # (2.2) ith char and jth char is not same
                    matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
        
        return matrix[-1][-1]
    
    
# Time: O(M*N)
# Space: O(M*N)


# Length of Longest Common Substring
class Solution:
    def longestCommonSubsequence(self, text1, text2):
        # (0) edge case
        if not text1 or not text2:
            return 0
        
        # (1) initialize a 2D DP array with all 0s
        matrix = [[0 for l in range(len(text1)+1)] for l in range(len(text2)+1)]
        
        # (2) fill 2D DP array, i and j are indice of DP array
        result = 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if text1[j-1] == text2[i-1]:               # (2.1) ith char and jth char is same
                    matrix[i][j] = matrix[i-1][j-1] + 1
                    result = max(result, matrix[i][j])
                else:                                      # (2.2) ith char and jth char is not same
                    matrix[i][j] = 0
        
        return result
    
# Time: O(M*N)
# Space: O(M*N)