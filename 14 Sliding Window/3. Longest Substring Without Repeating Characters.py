# 维护一个滑动窗口，窗口内的都是没有重复的字符，去尽可能的扩大窗口的大小，窗口不停的向右滑动。
# （1）如果当前遍历到的字符从未出现过，那么直接扩大右边界；
# （2）如果当前遍历到的字符出现过，则缩小窗口（左边索引向右移动），然后继续观察当前遍历到的字符；
# （3）重复（1）（2），直到左边索引无法再移动；
# （4）维护一个结果 res，每次用出现过的窗口大小来更新结果 res，最后返回 res 获取结果。

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # (0) edge case
        if not s:
            return 0
        
        # (1) initialize the left pointer, cur_len and max_len, and maintain a set
        lookup = set()
        left, cur_len, max_len = 0, 0, 0
        
        # (2) traverse the string to compare if letters are same with cur_len
        for r in range(len(s)):
            cur_len += 1
            while s[r] in lookup:       # (2.1) when the letter is in the set
                lookup.remove(s[left])  # (2.1.1) remove the leftmost letter 
                cur_len -= 1            # (2.1.2) update cur_len
                left += 1               # (2.1.3) update l += 1
            
            lookup.add(s[r])            # (2.2) add the letter to the set if it is not in set
            
            if cur_len > max_len:       # (2.3) update max_len
                max_len = cur_len
        
        # (3) return max_len
        return max_len

# Time: O(N), since traverse once.
# Space: O(N) for set.
# Note: (2.1) must be in front of (2.2) because we need to judge if the letter is a new one