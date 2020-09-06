# Given an array of integers arr, you are initially positioned at the first index of the array.
# In one step you can jump from index i to index:
# i + 1 where: i + 1 < arr.length.
# i - 1 where: i - 1 >= 0.
# j where: arr[i] == arr[j] and i != j.

# Return the minimum number of steps to reach the last index of the array.

# Notice that you can not jump outside of the array at any time.

# Example 1:
# Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
# Output: 3
# Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.

# Example 2:
# Input: arr = [7]
# Output: 0
# Explanation: Start index is the last index. You don't need to jump.

# Example 3:
# Input: arr = [7,6,9,6,9,6,9,7]
# Output: 1
# Explanation: You can jump directly from index 0 to index 7 which is last index of the array.

# Example 4:
# Input: arr = [6,1,9]
# Output: 2

# Example 5:
# Input: arr = [11,22,7,7,7,7,7,7,7,22,13]
# Output: 3


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # (0) edge case
        if len(arr) < 2:
            return 0
        
        # (1) dictionary: {element:index}
        nei = collections.defaultdict(list)
        for i, x in enumerate(arr):
            nei[x].append(i)             # {100:[0, 4], -23:[1, 2], 404:[3, 9], 23:[5, 6, 7], 3:[8]}
        
        # (2) initialize queue and track set
        queue = collections.deque([(0, 0)])
        num_met = set()
        pos_met = set()
        
        # (3) BFS
        while queue:
            # print(queue)
            pos, step = queue.popleft()         # state: position, step
            if pos == len(arr)-1: 
                return step
        
            pos_met.add(pos)                    # track explored positions

            num = arr[pos]                      # look for neighbors
            for p in [pos-1, pos+1] + nei[num] * (num not in num_met):    # remove duplicate number
                if 0 <= p < len(arr) and p not in pos_met:                # remove duplicate position
                    queue.append((p, step + 1))

            num_met.add(num)                    # track explored values

# Time: O(N)
# Space: O(N)