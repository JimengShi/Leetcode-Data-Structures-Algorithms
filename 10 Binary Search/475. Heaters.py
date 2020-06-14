from bisect import bisect
class Solution: 
    def findRadius(self, house, heater):
        heater.sort()
        ans = 0

        for h in house:      
            hi = bisect(heater, h)                             # for each house，find 1st heater >= house

            l_heater = heater[hi-1] if hi-1 >= 0 else float('-inf')

            r_heater = heater[hi] if hi < len(heater) else float('-inf')

            ans = max(ans, min(h - l_heater, r_heater - h))

        return ans
    
