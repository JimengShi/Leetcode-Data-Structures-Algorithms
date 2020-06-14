class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def check(x):
            """
            Return min number of swaps if one could make all elements in A or B equal to x.
            Else return -1.
            """
            # how many rotations should be done to have all elements in A or B == x
            rotations_a = rotations_b = 0
            for i in range(n):
                if A[i] != x and B[i] != x:        # rotations coudn't be done
                    return -1
                elif A[i] != x:                    # A[i] != x and B[i] == x
                    rotations_a += 1
                elif B[i] != x:                    # A[i] == x and B[i] != x   
                    rotations_b += 1
                    
            # min number of rotations to have all elements equal to x in A or B
            return min(rotations_a, rotations_b)
    
        n = len(A)
        rotations = check(A[0])
        # If one could make all elements in A or B equal to A[0]
        if rotations != -1:
            return rotations 
        # If one could make all elements in A or B equal to B[0]
        else:
            return check(B[0])
        

# A = [2, 1, 2, 4, 2, 2]
# B = [5, 2, 6, 2, 3, 2]
# the final same elements must be A[0] or B[0] or we just return -1.

# Time: O(N) since here one iterates over the arrays not more than two times.
# Space: O(1) since it's a constant space solution.