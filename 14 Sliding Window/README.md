# Type 1: Changeable Window Size
**Python Template:**
```Python
class Solution:
    def functionName(self, s, k):
        # (1) initialization
        l = 0
        count_dict = {}
        max_len = 0
        
        # (2) traverse the string or array to count
        for r in range(len(s)):
            count_dict[s[r]] = count_dict.get(s[r], 0) + 1
            while window condition is not satisfied:          # (2.1) window condition is not satisfied
                count_dict[s[l]] -= 1
                if count_dict[s[l]] == 0:
                    del count_dict[s[l]]
                l += 1
            max_len = max(max_len, r-l+1)                     # (2.2) window condition is satisfied
            
        # (3) return the result
        return max_len
```

| Question |    Solution   |  Difficulty |
|----------|:-------------|:------:|
| [Leecode](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/)    |  [340. Longest Substring with At Most K Distinct Characters](https://github.com/JimengShi/Leetcode-Data-Structures-Algorithms/blob/master/14%20Sliding%20Window/340.%20Longest%20Substring%20with%20At%20Most%20K%20Distinct%20Characters.py) | Medium |
| [Leecode](https://leetcode.com/problems/fruit-into-baskets/)    |  [904. Fruit Into Baskets](https://github.com/JimengShi/Leetcode-Data-Structures-Algorithms/blob/master/14%20Sliding%20Window/904.%20Fruit%20Into%20Baskets.py) | Medium |
| [Leecode](https://leetcode.com/problems/longest-repeating-character-replacement/)    |  [424. Longest Repeating Character Replacement](https://github.com/JimengShi/Leetcode-Data-Structures-Algorithms/blob/master/14%20Sliding%20Window/424.%20Longest%20Repeating%20Character%20Replacement.py) | Medium |
| [Leecode](https://leetcode.com/problems/subarrays-with-k-different-integers/)    |  [992. Subarrays with K Different Integers](https://github.com/JimengShi/Leetcode-Data-Structures-Algorithms/blob/master/14%20Sliding%20Window/992.%20Subarrays%20with%20K%20Different%20Integers.py) | Hard |
| [Leecode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)    |  [3. Longest Substring Without Repeating Characters](https://github.com/JimengShi/Leetcode-Data-Structures-Algorithms/blob/master/14%20Sliding%20Window/3.%20Longest%20Substring%20Without%20Repeating%20Characters.py) | Medium |



# Type 2: Unchangeable Window Size

| Question |    Solution   |  Difficulty |
|----------|:-------------|:------:|
| [Leecode](https://leetcode.com/problems/sliding-window-maximum/)    |  [239. Sliding Window Maximum](https://github.com/JimengShi/Leetcode-Data-Structures-Algorithms/blob/master/14%20Sliding%20Window/239.%20Sliding%20Window%20Maximum.py) | Hard |
| [Leecode](https://leetcode.com/problems/sliding-window-median/)    |  [480. Sliding Window Median](https://github.com/JimengShi/Leetcode-Data-Structures-Algorithms/blob/master/14%20Sliding%20Window/480.%20Sliding%20Window%20Median.py) | Hard |
| [Leecode](https://leetcode.com/problems/find-all-anagrams-in-a-string/)    |  [438. Find All Anagrams in a String](https://github.com/JimengShi/Leetcode-Data-Structures-Algorithms/blob/master/14%20Sliding%20Window/438.%20Find%20All%20Anagrams%20in%20a%20String.py) | Medium |
| [Leecode](https://leetcode.com/problems/permutation-in-string/)    |  [567. Permutation in String](https://github.com/JimengShi/Leetcode-Data-Structures-Algorithms/blob/master/14%20Sliding%20Window/567.%20Permutation%20in%20String.py) | Medium |