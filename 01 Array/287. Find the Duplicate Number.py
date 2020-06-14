# Method 1: Sorting
class Solution:
    def findDuplicate(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]

# Time: O(nlogn)
# Space: O(1)            
            
            
# Method 2: Set           
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

# Time: O(n)
# Space: O(n)


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # start hopping from Node_#0
        slow, fast = 0, 0
		
		# for locating start node of cycle
        check = 0
        
		# Step 1: Cycle detection: Let slow jumper and fast jumper meet somewhere in the cycle 
        while True:
			# slow jumper hops 1 step, while fast jumper hops two steps forward.
            slow = nums[ slow ]
            fast = nums[ nums[fast] ]
            
            if slow == fast:
                break
        
		
		# Step 2: Locate the start node of cycle (i.e., the duplicate number)
        while True:
            slow = nums[ slow ]
            check = nums[ check ]
            
            if slow == check:
                break
        
        return check
    
# Time: O(n)
# Space: O(1)