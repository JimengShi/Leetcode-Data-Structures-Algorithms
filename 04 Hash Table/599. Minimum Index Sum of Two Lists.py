class Solution(object):
    def findRestaurant(self, A, B):
        # (0) preprocess: create a dictionary for array A
        Aindex = { u:i for i, u in enumerate(A)}
        
        # (1) initialize data structure
        index_sum = 1e9        # 1 * 10^9
        ans = []

        # (2) find optimal index sum
        for j, v in enumerate(B):            # j: index of B value in B
            i = Aindex.get(v, 1e9)           # i: index of B value in A
            if i + j < index_sum:
                index_sum = i + j
                ans = [v]
            elif i + j == index_sum:
                ans.append(v)
        
        # (3) return result
        return ans
    
# Time: O(max(M,N))
# Space: O(min(M,N))