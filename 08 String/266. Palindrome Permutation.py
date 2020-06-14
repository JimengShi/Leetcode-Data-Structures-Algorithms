class Solution:
    def canPermutePalindrome(self, s: str) -> bool:  
        count = defaultdict(int)
        oddchar = 0
        for char in s:
            if count[char] == 1:
                count[char] -= 1
                oddchar -= 1
            else:
                count[char] = 1
                oddchar += 1

        if oddchar > 1:
                return False
        return True

# Time: O(N)
# Space: O(N)
    
# defaultdict(<class 'int'>, {})
# defaultdict(<class 'int'>, {'c': 1})
# oddchar: 1
# defaultdict(<class 'int'>, {'c': 1, 'a': 1})
# oddchar: 2
# defaultdict(<class 'int'>, {'c': 1, 'a': 1, 'r': 1})
# oddchar: 3
# defaultdict(<class 'int'>, {'c': 1, 'a': 1, 'r': 1, 'e': 1})
# oddchar: 4
# defaultdict(<class 'int'>, {'c': 1, 'a': 1, 'r': 0, 'e': 1})
# oddchar: 3
# defaultdict(<class 'int'>, {'c': 1, 'a': 0, 'r': 0, 'e': 1})
# oddchar: 2
# defaultdict(<class 'int'>, {'c': 0, 'a': 0, 'r': 0, 'e': 1})
# oddchar: 1
# True