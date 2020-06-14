class Solution(object):
    def isHappy(self, n: int) -> bool:    
        seen = set()

        while n not in seen:
            seen.add(n)
            n = sum([int(x)**2 for x in str(n)])
            print(n)
        return n == 1
    
# Time: O(logN)
# Space: O(1)
                
                
class Solution(object):
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1
    
# Time: O(logN)
# Space: O(1)