class Solution:
    def findMin(self, num):
        # (0) edge case
        if not num:
            return
        
        # (1) two pointers and while loop for binary search
        left, right = 0, len(num) - 1
        while left+1 < right:
            if num[left] < num[right]:              # no rotation
                return num[left]
            
            mid = left + (right - left) // 2
            if num[mid] > num[left] :
                left = mid
            elif num[mid] == num[left]:             # remove the duplicate
                left += 1
            else:
                right = mid

        # (2) return result when jump out of while loop: [L,R]
        return min(num[left], num[right])
    
# Time: O(logn)
# Space: O(1)