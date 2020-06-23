# Problem

# There are given n ropes of different lengths, we need to connect these ropes into one rope. The cost to connect two ropes is equal to sum of their lengths. We need to connect the ropes with minimum cost.
# For example if we are given 4 ropes of lengths 4, 3, 2 and 6. We can connect the ropes in following ways.
# 1) First connect ropes of lengths 2 and 3. Now we have three ropes of lengths 4, 6 and 5.
# 2) Now connect ropes of lengths 4 and 5. Now we have two ropes of lengths 6 and 9.
# 3) Finally connect the two ropes and all ropes have connected.
# Total cost for connecting all ropes is 5 + 9 + 15 = 29.


import heapq
def ropeCost(ropes):
    # (0) edge case
    if len(ropes) <= 1:
        return 0
    
    # (1) build heap
    heapq.heapify(ropes)
    
    # (2) greedy algorithm: mimimum cost if get number from short to long
    total = 0
    while ropes:
        first = heapq.heappop(ropes)     # greedy: get the first smallest
        second = heapq.heappop(ropes)    # greedy: get the second smallest
        local = first + second
        total += local
        if not ropes:
            break
            
        heapq.heappush(ropes, local)
    
    # (3) return result total cost
    return total

# Time: O(NlogN)
# Space: O(N)  