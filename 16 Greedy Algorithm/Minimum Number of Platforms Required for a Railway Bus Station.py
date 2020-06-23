# Problem
# Given arrival and departure times of all trains that reach a railway station, find the minimum number of platforms required for the railway station so that no train waits. We are given two arrays which represent arrival and departure times of trains that stop.

# Input:
# arr[] = {9:00, 9:40, 9:50, 11:00, 15:00, 18:00}
# dep[] = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00}

# Output: 3
# There are at-most three trains at a time (time between 11:00 to 11:20)


def findPlatform(arr, dep, n):
    # (0) edge case
    if not arr or nor dep:
        return 0
    
    # (1) sort arr and dep
    arr.sort()
    dep.sort()
  
    # (2) initialize plat_needed indicates number of platforms needed at a time
    plat_needed = 0
    result = 0
    i, j = 0, 0

    # (3) greedy
    while i < n and j < n:
        if arr[i] < dep[j]:
            plat_needed += 1
            result = max(result, plat_needed)
            i += 1
        else:
            plat_needed -= 1                   # minus 1: means we don't need a platform right now
            j += 1
    
    # (4) return result
    return result


# Time: O(N)
# Space: O(1)


# Example:
# arr = [900, 940, 950, 1100, 1500, 1800]
# dep = [910, 1200, 1120, 1130, 1900, 2000]
# n = len(arr)
# findPlatform(arr, dep, n)