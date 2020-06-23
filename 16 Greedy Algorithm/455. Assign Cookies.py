class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # (0) edge case
        if not g or not s:
            return 0
        
        # (1) sort and initialize variable
        g.sort()
        s.sort()
        happy = 0
        child, cookie = 0, 0
        
        # (2) greedy: small cookies for small standard
        while child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]:
                happy += 1
                child += 1
            cookie += 1
        
        # (3) return result
        return happy
    
# Time: O(nlogn)
# Space O(1)