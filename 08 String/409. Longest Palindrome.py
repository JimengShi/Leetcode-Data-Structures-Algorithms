from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        counter = Counter(s)
        for key in counter.keys():
            v = counter[key]
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
                
        return ans

# s = "abccccdd"  
# Counter({'c': 4, 'd': 2, 'a': 1, 'b': 1})
# keep even first (ans += v // 2 * 2), 
# then determine if v is odd or even, it's even --> ans += 1

# Time: O(N), where N is the length of s. We need to count each letter.
# Space: O(1), the space for our count, as the alphabet size of s is fixed. We should also consider that in a bit complexity model, technically we need O(logN) bits to store the count values.

