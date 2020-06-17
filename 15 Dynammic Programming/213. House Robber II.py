## APPROACH : DP ##
## LOGIC ##
## 1. Only 2 scenarios possible 
##     a) Rob 1st and donot rob last 
##     b) Rob last and donot rob first. 
## We take maximum of both cases.


class Solution:
    def rob(self, nums: List[int]) -> int:
        def house_robber(nums):
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], nums[i]+dp[i-2])
            return max(dp[-1], dp[-2])
        
        if len(nums) <= 2: 
            return max([0] + nums)
        return max( house_robber(nums[1:]), house_robber(nums[:-1]) )  

# if robbing 1st house
#                 rob 1     not rob 1    
# f(1,n) = max(  f(1,n-1),   f(2,n)   )


class Solution:
    def rob(self, nums: List[int]) -> int:
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
        
        if len(nums) <= 2: 
            return max([0] + nums)
        return max( house_robber(nums[1:]), house_robber(nums[:-1]) )