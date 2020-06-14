# Method 1: transfer number into string
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]
    
# Time: O(N)
# Space: O(1)



# Method2:
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # (1) initialize output and input
        opt = 0
        ipt = abs(x)                     
        
        # (2) reverse
        while ipt != 0:
            remainder = ipt % 10        # (2.1) get the remainder
            opt = opt * 10 + remainder  # (2.2) update output in a reversed order
            ipt = int(ipt / 10)         # (2.3) update input, <==> 'ipt = ipt // 10' 取整

        # (3) return the result by comparing input x and output opt
        if x >= 0 and x == opt:         
            return True
        else:
            return False

# Time: O(N)
# Space: O(1)

# 123  -->  321
# initialize input = 123, output = 0
# remainder:       3   2    1
#    output:   0   3   32   321
#     input: 123  12   1    0
# False