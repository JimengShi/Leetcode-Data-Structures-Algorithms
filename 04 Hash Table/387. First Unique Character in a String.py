class Solution:
    def firstUniqChar(self, s: str) -> int:
        # initialize data structure
        index = []
        letters = 'abcdefghijklmnopqrstuvwxyz'
        
        # find index of all unique character in string
        for l in letters:
            if s.count(l) == 1:
                index.append(s.index(l)) 
        
        # return result
        if len(index) > 0:
            return min(index)
        return -1

# # Time: O(N)
# # Space: O(N)
    

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # (1) initialize data structure
        arr = [0 for i in range(26)]     # arr = [0] * 26
        
        # (2) first for loop to put each letter into array
        for i in range(len(s)):
            arr[ord(s[i])-97] += 1
        
        # (3) second for loop to check if the freq is 1
        for j in range(len(s)):
            if arr[ord(s[j])-97] == 1:
                return j
        
        # (4) return -1 if it does not exist
        return -1
    
# # Time: O(N)
# # Space: O(N)



class Solution:
    def firstUniqChar(self, s: str) -> int:
        # (1) initialize data structure
        dic = {}   # arr = [0] * 26
        
        # (2) first for loop to put each letter into array
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        print(dic)
        
        # (3) second for loop to check if the freq is 1
        for key, val in dic.items():
            if val == 1:
                print(key)
                return s.index(key)
        
        # (4) return -1 if it does not exist
        return -1