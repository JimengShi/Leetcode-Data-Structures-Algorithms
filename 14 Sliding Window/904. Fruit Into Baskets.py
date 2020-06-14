# nums = [3, 3, 1, 2, 1, 1, 2]

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        # (1) initialize an empty dictionary and two pointers
        count = collections.Counter()
        ans = left = 0
        
        # (2) traverse the tree list
        for right, x in enumerate(tree):
            count[x] += 1                       # (2.1) count of each element --> window candidate
            while len(count) >= 3:              # (2.2) len(count) >= 3       --> greedy minimize
                count[tree[left]] -= 1
                if count[tree[left]] == 0:
                    del count[tree[left]]
                left += 1
            ans = max(ans, right - left + 1)    # (2.3) update ans (window sizea)
        
        # (3) return result
        return ans

# Time: O(N), where N is the length of tree.
# Space: O(N) for dictionary.


class Solution:
    def atMostK(self, nums, K):
        counter = collections.Counter()
        res = i = 0
        for j in range(len(nums)):
            if counter[nums[j]] == 0:
                K -= 1
            counter[nums[j]] += 1
            while K < 0:
                counter[nums[i]] -= 1
                if counter[nums[i]] == 0:
                    K += 1
                i += 1
            res = max(res, j - i + 1)
        return res

    def totalFruit(self, tree: List[int]) -> int:
        return self.atMostK(tree, 2)

# Time: O(N), where N is the length of tree.
# Space: O(N).