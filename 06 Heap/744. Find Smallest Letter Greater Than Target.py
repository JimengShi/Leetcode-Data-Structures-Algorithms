# Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

# Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

# Examples:
# Input:
# letters = ["c", "f", "j"]
# target = "a"
# Output: "c"

# Input:
# letters = ["c", "f", "j"]
# target = "c"
# Output: "f"

# Input:
# letters = ["c", "f", "j"]
# target = "d"
# Output: "f"

# Input:
# letters = ["c", "f", "j"]
# target = "g"
# Output: "j"

# Input:
# letters = ["c", "f", "j"]
# target = "j"
# Output: "c"

# Input:
# letters = ["c", "f", "j"]
# target = "k"
# Output: "c"

# O(n) / O(1)
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        for c in letters:
            if c > target:
                return c
        return letters[0]
    
# O(logN) / O(1)
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # (1) initialize left and right pointers
        l, r = 0, len(letters)-1
        
        # (2) edge case
        if target < letters[l] or target >= letters[r]:
            return letters[l]

        # (3) binary search
        while l <= r:
            middle =  (l + r) // 2
            candidate = letters[middle]
            
            if target < candidate: 
                r = middle - 1
            
            if target >= candidate:
                l = middle + 1
        
        return letters[l]