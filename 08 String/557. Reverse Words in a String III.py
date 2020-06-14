class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([seg[::-1] for seg in s.split()])
    
# Time: O(N)    
# Space: O(N)


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')       # separate string based on space
        l = []
        for seg in s:
            l.append(seg[::-1])
        return ' '.join(l)
    
# Time: O(N)    
# Space: O(N)