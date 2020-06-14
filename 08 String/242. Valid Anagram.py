# Method 1: sorting
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
# Time: O(nlogn)
# Space: O(1)
    

# Method 2: hashtable
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:   
        dic1, dic2 = {}, {}
        
        for item in s:
            dic1[item] = dic1.get(item, 0) + 1
        for item in t:
            dic2[item] = dic2.get(item, 0) + 1
            
        return dic1 == dic2
    
    
from collections import Counter
def areAnagram(str1, str2):
    return Counter(str1) == Counter(str2)

# Time: O(n)
# Space: O(1)