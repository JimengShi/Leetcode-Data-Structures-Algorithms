# Problem
# Assume there exist n activities with each of them being represented by a start time si and finish time fi. 
# Two activities i and j are said to be non-conflicting if si ≥ fj or sj ≥ fi. 
# The activity selection problem consists in finding the maximal solution set (S) of non-conflicting activities, 
# or more precisely there must exist no solution set S' such that |S'| > |S| in the case that multiple maximal solutions have equal sizes.

def printMaxActivities(acts):
    n = len(acts)
    sort_acts = sorted(acts, key=lambda tup: tup[1])
    print('sorted_acts:', sort_acts)
    
    prev = sort_acts[0]
    print(prev)
    
    for curr in sort_acts:
        if curr[0] >= prev[1]:   # greedy: curr start time >= prev finish time
            print(curr)
            prev = curr

# Time: O(nlogn) + O(n)
# Space: O(n)


# Example:
# acts = [(0,6), (3,4), (1,2), (5,7), (8,9), (5,9)]
# printMaxActivities(acts)

# sorted_acts: [(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]
# (1, 2)
# (3, 4)
# (5, 7)
# (8, 9)