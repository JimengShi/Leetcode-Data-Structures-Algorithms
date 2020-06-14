class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ls = [s[i:i+2*k] for i in range(0, len(s), 2*k)]  # segment into chunks of length 2k
        res = ''
        for seg in ls:
            res += seg[:k][::-1]     # reverse the first k characters of each chunk
            if len(seg) > k:
                res += seg[k:]       # append the rest of the chunk if there is any
                
        return res
    
# Time: O(N)
# Space: O(N)