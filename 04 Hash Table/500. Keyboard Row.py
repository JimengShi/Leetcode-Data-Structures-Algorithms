# Method 1: Set
# class Solution:
#     def findWords(self, words: List[str]) -> List[str]:
#         # (1) create data structure
#         line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
#         res = []
        
#         # (2) traverse the input array
#         for word in words:
#             w = set(word.lower())
#             if w.issubset(line1) or w.issubset(line2) or w.issubset(line3):    # issubset()
#                 res.append(word)
                
#         # (3) return result
#         return res
    
# Time: O(N), N is the length of all letters in given array
# Space: O(N)


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        dic = {'q': 0, 'w': 0, 'e': 0, 'r': 0, 't': 0, 'u': 0, 'i': 0, 'o': 0, 'p': 0,'y': 0,
               'a': 1, 's': 1, 'd': 1, 'f': 1, 'g': 1, 'h': 1, 'j': 1, 'k': 1, 'l': 1,
               'z': 2, 'x': 2, 'c': 2, 'v': 2, 'b': 2, 'n': 2, 'm': 2}

        for word in words:
            word_lower = word.lower()
            temp = dic[word_lower[0]]
            is_one_row = True
            
            for e in word_lower:
                if dic[e] != temp:
                    is_one_row = False
                    break
            if is_one_row:
                ans.append(word)
        
        return ans
    
# Time: O(N), N is the length of all letters in given array
# Space: O(N)