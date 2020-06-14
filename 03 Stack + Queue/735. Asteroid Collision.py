class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # (1) initialize
        ans = []
        
        # (2) traverse asteroids
        for new in asteroids:
            # (2.1) new < 0 and ans[-1] > 0  <==> collision
            while ans and new < 0 < ans[-1]:   
                if ans[-1] == abs(new):        # case 1: abs(new) == ans[-1] 
                    ans.pop()
                elif ans[-1] < abs(new):       # case 2: abs(new) > ans[-1], [10, 2]  -5
                    ans.pop()
                    continue
                # do nothing                   # case 3: abs(new) < ans[-1], [5, 10]  -5
                break 
                    
            # (2.2) (new > 0) or (ans is empty and new < 0)
            else:                              
                ans.append(new)
        
        # (3) return result
        return ans        
    
# Time: O(N), where N is the number of asteroids. Our stack pushes and pops each asteroid at most once.
# Space: O(N), the size of ans.