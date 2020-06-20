# class Solution:
#     def uniquePaths(self, m, n):
#         dp = [[1]*n for _ in range(m)]               # 2D matrix
        
#         for i in range(1, m):                        # i: row
#             for j in range(1, n):                    # j: column
#                 dp[i][j] = dp[i-1][j] + dp[i][j-1]

#         return dp[-1][-1]
    
# Time: O(M*N)
# Space: O(M*N)


class Solution:
    def uniquePaths(self, m, n):
        aux = [1 for x in range(n)]
        for i in range(1, m):
            for j in range(1, n):
                aux[j] = aux[j] + aux[j-1]
        return aux[-1]
    
# Time: O(M*N)
# Space: O(min(M,N))
