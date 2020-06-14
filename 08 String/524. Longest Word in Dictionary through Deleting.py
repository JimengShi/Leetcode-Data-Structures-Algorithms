# Method: two pointers
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        ans = ''
        for w in d:
            if self.issequence(s, w):
                if len(w) > len(ans):
                    ans = w
                elif len(w) == len(ans) and w < ans:
                    ans = w
        return ans
    
    def issequence(self, str1, str2):       # str1 --> long, str2 --> short
        i, j = 0, 0
        while i < len(str2) and j < len(str1):
            if str2[i] == str1[j]:
                i += 1
                j += 1
            else:
                j += 1
                
        return i == len(str2)
    
# Time: O(mn), m is the length of d, n is the length of string s
# Space: O(1)