class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        if A[0] == B[0]: 
            return self.frequency(A, B, A[0])
        return max(self.frequency(A, B, A[0]), self.frequency(A, B, B[0]))
        
    def frequency(self, A, B, num):
        top, bottom = 0, 0
        for i in range(len(A)):
            if A[i] != num and B[i] != num:
                return -1
            elif A[i] != num: 
                top += 1
            elif B[i] != num:
                bottom += 1
        return min(top, bottom)
        

# A = [2, 1, 2, 4, 2, 2]
# B = [5, 2, 6, 2, 3, 2]
# the final same elements must be A[0] or B[0] or we just return -1.

# Time: O(N) since here one iterates over the arrays not more than two times.
# Space: O(1) since it's a constant space solution.