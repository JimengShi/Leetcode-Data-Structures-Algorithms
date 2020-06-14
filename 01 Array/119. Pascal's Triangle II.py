class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for k in range(1, rowIndex + 1):         # k: from the 1st row to rowIndex row
            l = []
            for j in range(k+1):                 # j: from the 0th element to kth element on kth row
                if j == 0 or j == k:
                    l.append(1)
                else:
                    l.append(res[j-1] + res[j])
            res = l
            
        return res
    
# rowIndex k
# k = 0           1
# k = 1         1   1
# k = 2       1   2   1
# k = 3     1   3   3   1       
# k = 4   1   4   6   4   1
#         0   1   2   3   4  <--- j index
    
# Time: O(k^2)
# Space: O(k^2) for keeping only the latest generated row
    
    

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)
        for i in range(1, rowIndex):
            for j in range(i):
                row[i-j] += row[i-j-1]
        return row
    
# Time: O(k^2)
# Space: O(1) for keeping only the latest generated row