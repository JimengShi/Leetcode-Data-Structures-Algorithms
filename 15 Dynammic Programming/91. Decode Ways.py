# (0) If the string s is empty or null we return the result as 0.

# (1) Initialize dp array. dp[0] = 1 to provide the baton to be passed.
# (2) If the first character of the string is zero then no decode is possible, hence initialize dp[1] to 0, otherwise the first character is valid to pass on the baton, dp[1] = 1.

# (2) Iterate the dp array starting at index 2. The index i of dp is the i-th character of the string s, that is character at index i-1 of s.

#   (2.1) We check if valid single digit decode is possible. This just means the character at index s[i-1] is non-zero. Since we do not have a decoding for zero. If the valid single digit decoding is possible then we add dp[i-1] to dp[i]. Since all the ways up to (i-1)-th character now lead up to i-th character too.

#   (2.2) We check if valid two digit decode is possible. This means the substring s[i-2]s[i-1] is between 10 to 26. If the valid two digit decoding is possible then we add dp[i-2] to dp[i].

# (3) Once we reach the end of the dp array we would have the number of ways of decoding string s.

class Solution(object):
    def numDecodings(self, s):
        # (0) edge case
        if not s:
            return 0

        # (1) initialize DP array to store the subproblem results
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1   # decode a string of size 1 is 1 unless string is '0'

        # (2) iteratively compute dp
        for i in range(2, len(dp)):
            if s[i-1] != '0':                       # Check if single digit decode
                dp[i] += dp[i-1]

            two_digit = int(s[i-2 : i])             # Check if two digit decode
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]
                
        # (3) return result
        return dp[len(s)]
    
# Time: O(N)    
# Space: O(N)


class Solution(object):
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0
        
        dp = [1, 1]
        for i in range(1, len(s)):
            temp = 0
            if 1 <= int(s[i]) <= 9:
                temp = dp[1]
            if 10 <= int(s[i-1:i+1]) <= 26:
                temp += dp[0]
            dp = [dp[1], temp]
        return dp[1]
    
# Time: O(N)    
# Space: O(1)