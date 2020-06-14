# Method: hash table
class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        d = {}
        for index, item in enumerate(B):
            d[item] = index
            
        res = []
        for a in A:
            res.append(d[a])
        return res                          # return [d[a] for a in A]
    

# A  = [12, 28, 46, 32, 50]
# B  = [50, 12, 32, 46, 28]
# index: 0,  1,  2,  3,  4

# Time: O(n)
# Space: O(n)