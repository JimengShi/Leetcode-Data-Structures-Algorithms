# Method 1: sorting
class Solution:
    def findMin(self, li: List[int]) -> int:
	    li.sort()
	    return li[0]

# Time: O(nlogn)
# Space: O(1)


# Method 2: in
class Solution:
    def findMin(self, li: List[int]) -> int:
	    mini = li[0]
	    for i in li:
	        mini = min(mini, i)
	    return mini

# Time: O(n)
# Space: O(1)


# Method 3: binary search
class Solution:
    def findMin(self, li: List[int]) -> int:
        # (0) edge case
        if len(li) == 0:
            return -1

        # (1) two pointers and while loop
        l, r = 0, len(li)-1
        while l+1 < r:
            if li[l] < li[r]:
                return li[l]
            
            mid = (l+r) // 2
            if li[mid] >= li[l]:
                l = mid
            else:
                r = mid
        
        # (2) check boundary condition
        if li[l] < li[r]:
            return li[l]
        return li[r]

# Time: O(logn)
# Space: O(1)