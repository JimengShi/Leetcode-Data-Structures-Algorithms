# Type 1: Changeable Window Size
**Python Template:**
```Python
class Solution:
    def functionName(self, s, k):
        # (1) initialization
        l = 0
        count_dict = {}      # data strucuture here can be changed to others, such as set (e.g., Q3) or list (e.g., Q424).
        max_len = 0
        
        # (2) traverse the string or array to count
        for r in range(len(s)):
            count_dict[s[r]] = count_dict.get(s[r], 0) + 1
            while window condition is not satisfied:          # (2.1) window condition is not satisfied
                count_dict[s[l]] -= 1
                if count_dict[s[l]] == 0:
                    del count_dict[s[l]]
                l += 1
            max_len = max(max_len, r-l+1)                     # (2.2) window condition is satisfied. here can be changed to count_num += r-l+1 (e.g., Q992)
            
        # (3) return the result
        return max_len
```


| Question |    Solution   |  Difficulty |
|----------|:-------------|:------:|
| [Leecode](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/)    |  [340. Longest Substring with At Most K Distinct Characters](https://github.com/JimengShi/Leetcode-Data-Structures-Algorithms/blob/master/14%20Sliding%20Window/340.%20Longest%20Substring%20with%20At%20Most%20K%20Distinct%20Characters.py) | Medium |
| [Leecode](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/)    |  [159. Longest Substring with At Most Two Distinct Characters](https://github.com/JimengShi/Leetcode-Data-Structures-Algorithms/blob/master/14%20Sliding%20Window/159.%20Longest%20Substring%20with%20At%20Most%20Two%20Distinct%20Characters.py) | Medium |
| [Leecode](https://leetcode.com/problems/fruit-into-baskets/)    |  [904. Fruit Into Baskets](https://github.com/JimengShi/Leetcode-Data-Structures-Algorithms/blob/master/14%20Sliding%20Window/904.%20Fruit%20Into%20Baskets.py) | Medium |
| [Leecode](https://leetcode.com/problems/longest-repeating-character-replacement/)    |  [424. Longest Repeating Character Replacement](https://github.com/JimengShi/Leetcode-Data-Structures-Algorithms/blob/master/14%20Sliding%20Window/424.%20Longest%20Repeating%20Character%20Replacement.py) | Medium |
| [Leecode](https://leetcode.com/problems/replace-the-substring-for-balanced-string/)    |  [1234. Replace the Substring for Balanced String](https://github.com/JimengShi/Leetcode-Data-Structures-Algorithms/blob/master/14%20Sliding%20Window/1234.%20Replace%20the%20Substring%20for%20Balanced%20String.py) | Medium |
| [Leecode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)    |  [3. Longest Substring Without Repeating Characters](https://github.com/JimengShi/Leetcode-Data-Structures-Algorithms/blob/master/14%20Sliding%20Window/3.%20Longest%20Substring%20Without%20Repeating%20Characters.py) | Medium |
| [Leecode](https://leetcode.com/problems/subarrays-with-k-different-integers/)    |  [992. Subarrays with K Different Integers](https://github.com/JimengShi/Leetcode-Data-Structures-Algorithms/blob/master/14%20Sliding%20Window/992.%20Subarrays%20with%20K%20Different%20Integers.py) | Hard |
| [Leecode](https://leetcode.com/problems/minimum-size-subarray-sum/)    |  [209. Minimum Size Subarray Sum](https://github.com/JimengShi/Leetcode-Data-Structures-Algorithms/blob/master/14%20Sliding%20Window/209.%20Minimum%20Size%20Subarray%20Sum.py) | Medium |
| [Leecode](https://leetcode.com/problems/subarray-product-less-than-k/)    |  [713. Subarray Product Less Than K](https://github.com/JimengShi/Leetcode-Data-Structures-Algorithms/blob/master/14%20Sliding%20Window/713.%20Subarray%20Product%20Less%20Than%20K.py) | Medium |
| [Leecode](https://leetcode.com/problems/max-consecutive-ones-iii/)    |  [1004. Max Consecutive Ones III](https://github.com/JimengShi/Leetcode-Data-Structures-Algorithms/blob/master/14%20Sliding%20Window/713.%20Subarray%20Product%20Less%20Than%20K.py) | Medium |
| [Leecode](https://leetcode.com/problems/max-consecutive-ones-ii/)    |  [487. Max Consecutive Ones II](https://github.com/JimengShi/Leetcode-Data-Structures-Algorithms/blob/master/14%20Sliding%20Window/487.%20Max%20Consecutive%20Ones%20II.py) | Medium |
| [Leecode](https://leetcode.com/problems/permutation-in-string/)    |  [567. Permutation in String](https://github.com/JimengShi/Leetcode-Data-Structures-Algorithms/blob/master/14%20Sliding%20Window/1004.%20Max%20Consecutive%20Ones%20III.py) | Medium |
| [Leecode](https://leetcode.com/problems/max-consecutive-ones/)    |  [485. Max Consecutive Ones](https://github.com/JimengShi/Leetcode-Data-Structures-Algorithms/blob/master/14%20Sliding%20Window/485.%20Max%20Consecutive%20Ones.py) | Easy |
| [Leecode](https://leetcode.com/problems/longest-continuous-increasing-subsequence/)    |  [674. Longest Continuous Increasing Subsequence](https://github.com/JimengShi/Leetcode-Data-Structures-Algorithms/blob/master/14%20Sliding%20Window/674.%20Longest%20Continuous%20Increasing%20Subsequence.py) | Easy |
| [Leecode](https://leetcode.com/problems/implement-strstr/)    |  [28. Implement strStr()](https://github.com/JimengShi/Leetcode-Data-Structures-Algorithms/blob/master/14%20Sliding%20Window/28.%20Implement%20strStr().py) | Easy |
| [Leecode](https://leetcode.com/problems/binary-subarrays-with-sum/)    |  [930. Binary Subarrays With Sum](https://github.com/JimengShi/Leetcode-Data-Structures-Algorithms/blob/master/14%20Sliding%20Window/930.%20Binary%20Subarrays%20With%20Sum.py) | Easy |
| [Leecode](https://leetcode.com/problems/subarray-sum-equals-k/)    |  [560. Subarray Sum Equals K](https://github.com/JimengShi/Leetcode-Data-Structures-Algorithms/blob/master/14%20Sliding%20Window/560.%20Subarray%20Sum%20Equals%20K.py) | Midium |
| [Leecode](https://leetcode.com/problems/maximum-subarray/)    |  [53. Maximum Subarray](https://github.com/JimengShi/Leetcode-Data-Structures-Algorithms/blob/master/14%20Sliding%20Window/53.%20Maximum%20Subarray.py) | Easy |


# Type 2: Unchangeable Window Size
| Question |    Solution   |  Difficulty |
|----------|:-------------|:------:|
| [Leecode](https://leetcode.com/problems/sliding-window-maximum/)    |  [239. Sliding Window Maximum](https://github.com/JimengShi/Leetcode-Data-Structures-Algorithms/blob/master/14%20Sliding%20Window/239.%20Sliding%20Window%20Maximum.py) | Hard |
| [Leecode](https://leetcode.com/problems/sliding-window-median/)    |  [480. Sliding Window Median](https://github.com/JimengShi/Leetcode-Data-Structures-Algorithms/blob/master/14%20Sliding%20Window/480.%20Sliding%20Window%20Median.py) | Hard |
| [Leecode](https://leetcode.com/problems/find-all-anagrams-in-a-string/)    |  [438. Find All Anagrams in a String](https://github.com/JimengShi/Leetcode-Data-Structures-Algorithms/blob/master/14%20Sliding%20Window/438.%20Find%20All%20Anagrams%20in%20a%20String.py) | Medium |
| [Leecode](https://leetcode.com/problems/maximum-average-subarray-i/)    |  [643. Maximum Average Subarray I](https://github.com/JimengShi/Leetcode-Data-Structures-Algorithms/blob/master/14%20Sliding%20Window/643.%20Maximum%20Average%20Subarray%20I.py) | Easy |
| [Leecode](https://leetcode.com/problems/maximum-average-subarray-ii/)    |  [644. Maximum Average Subarray II](https://github.com/JimengShi/Leetcode-Data-Structures-Algorithms/blob/master/14%20Sliding%20Window/644.%20Maximum%20Average%20Subarray%20II.py) | Hard |



# Type 3: Minimum Window Substring/Subsequence
| Question |    Solution   |  Difficulty |
|----------|:-------------|:------:|
| [Leecode](https://leetcode.com/problems/minimum-window-substring/)    |  [76. Minimum Window Substring](https://github.com/JimengShi/Leetcode-Data-Structures-Algorithms/blob/master/14%20Sliding%20Window/76.%20Minimum%20Window%20Substring.py) | Hard |
| [Leecode](https://leetcode.com/problems/minimum-window-subsequence/)    |  [727. Minimum Window Subsequence](https://github.com/JimengShi/Leetcode-Data-Structures-Algorithms/blob/master/14%20Sliding%20Window/727.%20Minimum%20Window%20Subsequence.py) | Hard |
