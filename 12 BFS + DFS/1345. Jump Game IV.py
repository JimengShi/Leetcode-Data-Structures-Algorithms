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
            pos, step = queue.popleft()         # state: position, step
            if pos == len(arr)-1: 
                return step
            
            pos_met.add(pos)                    # track explored positions
            num = arr[pos]

            for p in [pos-1, pos+1] + nei[num] * (num not in num_met):
                if p in pos_met or not 0 <= p < len(arr): 
                    continue
                queue.append((p, step + 1))

            num_met.add(num)                    # track explored values

# Time: O(N)
# Space: O(N)