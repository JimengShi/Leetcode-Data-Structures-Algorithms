# Method 1: brute force
class Solution(object):
    def rotateString(self, A, B):
        if len(A) != len(B):
            return False
        if len(A) == 0:
            return True

        for s in range(len(A)):
            # for i in range(len(A)):
                if all(A[(s+i) % len(A)] == B[i] for i in range(len(A))):
                    return True
        return False
    
# Time: O(N^2), where N is the length of A. For each rotation s, we check up to N elements in A and B.
# Space: O(1). We only use pointers to elements of A and B.
    
    
    
# Method 2:
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return 0

        temp = A + A

        return temp.count(B) > 0
    

# A = 'abcde'  --->  AA = 'ab[cdeab]cde'
# B = 'cdeab'  --->          'cdeab'

# Time: O(N)
# Space: O(N)