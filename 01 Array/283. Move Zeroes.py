class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            # wait while we find a non-zero element to switch with you
            if nums[slow] != 0:
                slow += 1

            # keep going
            fast += 1

# Time complexity: O(n). Our fast pointer does not visit the same spot twice.
# Space complexity: O(1). All operations are made in-place