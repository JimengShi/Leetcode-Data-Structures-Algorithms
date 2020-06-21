# Method 1: Dynamic Programming
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # (0) edge case
        if not nums: 
            return 0
        
        # (1) initialize dp array
        dp = [1] * len(nums)
        
        # (2) update dp array with general formula
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:             # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                    dp[i] = max(dp[i], dp[j]+1)
        
        # (3) return result            
        return max(dp)
    
# Time complexity : O(n^2). Two loops of n are there.
# Space: O(n). dp array of size n is used.



# Method 2: Dynamic Programming with Binary Search
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # (0) edge case
        if len(nums) <= 1:
            return len(nums)
        
        # (1) initialize dp array
        dp = [0] * len(nums)
        
        # (2) update dp array with binary search
        size = 0
        for num in nums:
            l, r = 0, size-1
            while l <= r:
                mid = (l+r) // 2
                if dp[mid] >= num:
                    r = mid - 1
                else:
                    l = mid + 1

            dp[l] = num
            size = max(size, l+1)
            
        # (3) return result
        return size

# Time: O(nlogn). Binary search takes logn time and it is called n times.
# Space: O(n). dp array of size n is used.