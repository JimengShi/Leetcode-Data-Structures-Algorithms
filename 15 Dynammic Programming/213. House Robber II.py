# Only 2 scenarios possible, We take maximum of both cases.
# a) Rob 1st and donot rob last 
# b) Rob last and donot rob first. 

#                 rob 1     not rob 1    
# f(1,n) = max(  f(1,n-1),   f(2,n)   )


class Solution:
    def rob(self, nums: List[int]) -> int:
        # (0) edge case
        if len(nums) <= 2:
            return max([0] + nums)
        
        # (1) function for problem 198
        def house_robber(arr):
            n = len(arr)
            if n == 0:
                return 0
            if n == 1:
                return arr[0]

            dp = [ [0] * 2 for _ in range(n+1)]
            for i in range(1, n+1):
                dp[i][0] = max(dp[i-1][0], dp[i-1][1])  # forget it
                dp[i][1] = arr[i-1] + dp[i-1][0]        # let's do it
            return max(dp[n][0], dp[n][1]) 
        
        # (2) return Rob 1st and donot rob last and Rob last and donot rob first.
        return max( house_robber(nums[1:]), house_robber(nums[:-1]) )  

# Time: O(n)
# Space: O(n)


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2: 
            return max([0] + nums)
        
        def house_robber(nums):
            n = len(nums)
            if n == 0:
                return 0
            if n == 1:
                return nums[0]
            yes, no = 0, 0
            for i in nums: 
                no, yes = max(no, yes), i + no
            return max(no, yes)
        

        return max( house_robber(nums[1:]), house_robber(nums[:-1]) )
    
# Time: O(n)
# Space: O(1)