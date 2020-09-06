# Given two words (beginWord and endWord), and a dictionary's word list, 
# find the length of shortest transformation sequence from beginWord to endWord, such that:
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list.

# Note:
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.

# Example 1:
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", return its length 5.

# Example 2: 
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.


import string
class Solution:    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # (0) edge case
        if endWord not in wordList: 
            return 0
        
        # (1) transfer wordList to a set so that repeat check
        wordList = set(wordList)
        
        # (2) push beginword and the corresponding step into queue
        queue = [(beginWord, 1)]
        while queue:
            word, length = queue.pop(0)                     # (2.1) pop the 1st element in queue
            if word == endWord:                             # (2.2) stop condition
                return length
            for i in range(len(word)):                      # (2.3) traverse the word letters
                for char in string.ascii_lowercase:         #       or string.ascii_lowercase[:26]
                    tmp = word[:i] + char + word[i+1:]      # (2.4) tmp is transformed word
                    if tmp in wordList:
                        queue.append((tmp, length+1))
                        wordList.remove(tmp)
                        
        # (3) return results 0
        return 0
    
# Time: O(n*26*l), n is the length of wordList, l is the length of the word in wordList.
# Space: O(n).