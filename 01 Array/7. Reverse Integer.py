class Solution:
    def reverse(self, x: int) -> int:
        order = 0                           # output value, initial is 0
        num = abs(x)
        while num != 0:                     # reverse num and save it to order
            remainder = num % 10            # get the last digit of every num 
            order = order * 10 + remainder 	# move 1 digit to left
            num = int(num / 10)             # delete single digit and renew num
            
        if x > 0 and order < 2**31-1:
            return order
        elif x < 0 and order <= 2**31:
            return -order
        else:
            return 0
        
# Time: O(log(x)). There are roughly log10(x) digits in x.
# Space: O(1).