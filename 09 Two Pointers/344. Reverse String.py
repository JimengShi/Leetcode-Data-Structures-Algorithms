# Write a function that reverses a string. The input string is given as an array of characters char[].
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# You may assume all the characters consist of printable ascii characters.

# Example 1:
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]


# Method 1: two pointers
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s)-1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

# Time: O(N)
# Space: O(1)


# Method 2: stack
class Solution:
    def reverseString(self, s: List[str]) -> None:
        stack = []
        for i in s:
            stack.append(i)

        res = []
        while len(stack) != 0:
            res.append(stack.pop())
        return res
    
# Time: O(N)
# Space: O(N)