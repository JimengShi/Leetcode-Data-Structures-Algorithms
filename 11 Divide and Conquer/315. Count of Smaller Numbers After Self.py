class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    count[i] += 1

        return count

# Time: O(n^2)
# Space: O(n)


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def sort(enum):
            half = len(enum) // 2
            left, right = sort(enum[:half]), sort(enum[half:])
            m, n = len(left), len(right)
            
            i = j = 0
            while i < m or j < n:
                if j == n or i < m and left[i][1] <= right[j][1]:
                    smaller[left[i][0]] += j
                    enum[i+j] = left[i]
                    i += 1
                else:
                    enum[i+j] = right[j]
                    j += 1

            return enum

        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))    
        return smaller
    
# list(enumerate(nums))  -->  [(0, 5), (1, 2), (2, 6), (3, 1)]
# Time: O(nlogn)
# Space: O()