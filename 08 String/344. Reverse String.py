# Method 1: two pointers
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left = left + 1
            right = right - 1

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