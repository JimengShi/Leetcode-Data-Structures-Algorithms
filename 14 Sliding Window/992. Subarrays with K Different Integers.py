class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.atMostK(A, K) - self.atMostK(A, K - 1)

    def atMostK(self, A, K):
        count = collections.Counter()
        res = i = 0
        for j in range(len(A)):
            if count[A[j]] == 0: K -= 1
            count[A[j]] += 1
            while K < 0:
                count[A[i]] -= 1
                if count[A[i]] == 0: K += 1
                i += 1
            res += j - i + 1
        return res

    
    
import collections
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        
        ##for counting subarrays with at most K unique elements    
        c1 = collections.Counter()
        d1 = 0                      #num_distinct_1

        ##for counting subarrays with less than K unique elements
        c2 = collections.Counter()
        d2 = 0                      #num_distinct_2
        
        ans = 0
        left1 = left2 = 0
            
        for idx, num in enumerate(A):
            c1[num]+=1
            c2[num]+=1
            if c1[num]==1:
                d1+=1
            if c2[num]==1:
                d2+=1
                
            while d1>K:
                n = A[left1]
                c1[n]-=1
                if c1[n]==0:
                    d1-=1
                left1+=1
                
            while d2>=K:
                n = A[left2]
                c2[n]-=1
                if c2[n]==0:
                    d2-=1
                left2+=1
            
            ans += left2 - left1
        
        return ans
    
###O(n) sliding window solution