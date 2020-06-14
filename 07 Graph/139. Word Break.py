# Method 1: bfs with queue
# Time: O(n^2). For every starting index, the search can continue till the end of the given string.
# Space: O(n). Queue of at most n size is needed.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # (1) initialize a queue (keep string) and a set (avoid duplicate work)
        from collections import deque
        queue = deque([s])
        seen = set()
        
        # (2) traverse queue when it's not empty
        while queue:
            s = queue.popleft()              # (2.1) pop the 1st element in queue 
            for word in wordDict:
                if s.startswith(word):
                    new_s = s[len(word):]    # (2.2) chop off the front of string if it starts with a word in the dictionary
                    
                    if new_s == "":          # (2.3) If string becomes empty, that means word break succeeded
                        return True
                    
                    if new_s not in seen:    # (2.4) Keep a set of seen string states to avoid duplicate work.
                        queue.append(new_s) 
                        seen.add(new_s)
        return False

# Method 2: dfs with stack
# Time: O(n^2). For every starting index, the search can continue till the end of the given string.
# Space: O(n). Queue of at most n size is needed.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        stack = [s]
        seen = set() 
        while stack:
            s = stack.pop()
            for word in wordDict:
                if s.startswith(word):
                    new_s = s[len(word):]
                    
                    if new_s == "": 
                        return True
                    
                    if new_s not in seen:
                        stack.append(new_s)
                        seen.add(new_s)
        return False

# Method 3: dp
# Time: O(n^2). Two loops are their to fill dp array.
# Space: O(n). Length of pp array is n+1n+1.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordDict = set(wordDict)
        
        # dp[i] means if s[:i] meets
        dp = [False for _ in range(n+1)]
        dp[0] = True
        
        for i in range(1, n+1):
            for j in range(i):
                sub_string = s[j:i]
                if dp[j] and sub_string in wordDict:
                    dp[i] = True
                    break
        return dp[-1]