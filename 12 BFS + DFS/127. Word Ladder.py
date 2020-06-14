# Time O(n26^l), n is the length of wordList, l is the length of the word in wordList.
# Space O(n).
class Solution    
    def ladderLength(self, beginWord str, endWord str, wordList List[str]) - int
        # (0) edge case
        if endWord not in wordList 
            return 0
        
        # (1) transfer wordList to a set so that repeat check
        wordList = set(wordList)
        
        # (2) push beginword and the corresponding step into queue
        queue = [(beginWord, 1)]
        while queue
            word, d = queue.pop(0)                          # (2.1) pop the 1st element in queue
            if word == endWord                             # (2.2) stop condition
                return d
            for i in range(len(word))                      # (2.3) traverse the word letters
                for char in 'abcdefghijklmnopqrstuvwxyz'   #       string.ascii_lowercase
                    tmp = word[i] + char + word[i+1]      # (2.4) tmp is transformed word
                    if tmp in wordList
                        queue.append([tmp, d+1])
                        wordList.remove(tmp)
                        
        # (3) return results 0
        return 0

    
from collections import deque
class Solution 
    def ladderLength(self, beginWord, endWord, wordList)
        # (0) edge case
        if endWord not in wordList 
            return 0
        
        # (1) transfer wordList to a set to avoid duplicates
        wordSet = set(wordList)
        
        # (2) push beginword and the corresponding step into queue
        queue = deque([[beginWord, 1]])
        while queue
            word, length = queue.popleft()
            if word == endWord
                return length
            for i in range(len(word))
                for char in 'abcdefghijklmnopqrstuvwxyz'
                    next_word = word[i] + char + word[i+1]
                    if next_word in wordSet
                        wordSet.remove(next_word)
                        queue.append([next_word, length + 1])
        
        # (3) return results 0
        return 0