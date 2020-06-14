# Similar to problem 46
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        self.res = []

        def dfs(n, strr):
            if len(strr) == n:
                self.res.append(strr)

            for i in range(1, n+1):
                if str(i) in strr: 
                    continue

                strr += str(i)
                dfs(n, strr)
                strr = strr[:-1]      # be equivalent to strr.pop(the last element)
                
        dfs(n, "")
        return self.res[k-1]
    
# Time: O(N x N!). Initially we have N choices, and in each choice we have (N - 1) choices, and so on. Notice that at the end when adding the list to the result list, it takes O(N).
# Space：O(N x N!). Since we have N! solutions and each of them requires N space to store elements.   