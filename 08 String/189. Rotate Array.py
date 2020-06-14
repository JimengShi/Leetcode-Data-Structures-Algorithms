class Solution  
    def rotate(self, nums List[int], k int) - None
        size = len(nums)
        if k  size           # eliminate redundant rotation which is over size
            k = k % size
        nums[] = nums[-k] + nums[-k]
        
# Time O(n), because to get k item with slice takes O(k) time
# Space O(1)
        


class Solution
    def reverse(self, nums List[int], start, end)
		# reverse array elements within [start, end] interval
        while start  end  
            nums[start], nums[end] = nums[end], nums[start] 
            start += 1
            end -= 1
            
    def rotate(self, nums List[int], k int) - None
        size = len(nums)
        if k  size           # eliminate redundant rotation which is over size
            k = k % size 
        
        self.reverse( nums, 0, size-1)  # reverse all elements 
        self.reverse( nums, 0, k-1)     # reverse first k elements
        self.reverse( nums, k, size-1)  # reverse last (size - k) elements 


# reverse three times
# [1, 2, 3, 4, 5, 6, 7]
# [7, 6, 5,4, 3, 2, 1]
# [5, 6, 5,1, 2, 3, 4]
    
# Time O(n)
# Space O(1)