# Method 1: Two-pass algorithm using counting sort.
class Solution(object):
    def sortColors(self, nums):
        # (1) initialize the appearing time of three colors == 0
        count = [0] * 3                
        
        # (2) iterate the array to count number of 0's, 1's, and 2's
        for num in nums:
            count[num] += 1
        
        # (3) overwrite array with total number of 0's, then 1's and followed by 2's
        i = 0
        for j in range(3):             # three colors
            for _ in range(count[j]):
                nums[i] = j
                i += 1

# Time: O(N), N is the length of the input array
# Space: O(N), save count of three color and reformed array



# Method 2: One-pass algorithm
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # (1) initialize rightmost boundary of zeros and leftmost boundary of twos 
        p0 = 0                 # for all idx < p0: nums[idx < p0] = 0
        curr = 0               # curr is index of element under consideration
        p2 = len(nums) - 1     # for all idx > p2: nums[idx > p2] = 2

        # (2) traverse the array
        while curr <= p2:
            # (2.1) If nums[curr] = 0, swap curr and p0 elements and move both pointers to right
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            
            # (2.2) If nums[curr] = 2, swap curr and p2 elements, and Move pointer p2 to left
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
                
            # (2.3) If nums[curr] = 1 : move pointer curr to the right.
            else:
                curr += 1


# Time: O(N) since it's one pass along the array of length N.
# Space: O(1) since it's a constant space solution.