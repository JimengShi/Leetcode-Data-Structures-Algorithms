# Method 1: Dictionary or set
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()
        res = []
        for num in nums:
            if num in seen:
                res.append(num)
            seen.add(num)
        return res
    
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:    
        # (1) Hash table, we can also use a set since we are not concerned with the frequency of numbers
        hash_table = {}
        res = []
        
        # (2) Add each of the numbers to the hash table
        for num in nums:
            hash_table[num] = hash_table.get(num, 0) + 1
            if hash_table[num] >= 2:
                res.append(num)
            
        # (3) return the result
        return res

# Time: O(n)
# Space: O(n)


# Method 2: In place
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # (1) initialize an empty list
        res = []
        
        # (2) traverse the array, for number k, its home index is (k-1)
        for idx, cur_num in enumerate(nums):
            home_idx = abs(cur_num) - 1
            
            if nums[home_idx] < 0:   # nums[home_idx] has been visited before (home_idx + 1) is repeated twice
                res.append( home_idx + 1 )
            else:
                nums[home_idx] = -nums[home_idx]  # Use negative sign to mark that nums[home_idx] as visited
        
        # (3) return result
        return res
    

# Time: O(n)
# Space: O(1)

# nums = [4, 3, 2, 7, 8, 2, 3, 1]
# index:  0  1  2  3  4  5  6  7

# iteration: 0
# home_index: 3
# nums: [4, 3, 2, -7, 8, 2, 3, 1]
# -----
# iteration: 1
# home_index: 2
# nums: [4, 3, -2, -7, 8, 2, 3, 1]
# -----
# iteration: 2
# home_index: 1
# nums: [4, -3, -2, -7, 8, 2, 3, 1]
# -----
# iteration: 3
# home_index: 6
# nums: [4, -3, -2, -7, 8, 2, -3, 1]
# -----
# iteration: 4
# home_index: 7
# nums: [4, -3, -2, -7, 8, 2, -3, -1]
# -----
# iteration: 5
# home_index: 1
# res: [2]
# -----
# iteration: 6
# home_index: 2
# res: [2, 3]
# -----
# iteration: 7
# home_index: 0
# nums: [-4, -3, -2, -7, 8, 2, -3, -1]