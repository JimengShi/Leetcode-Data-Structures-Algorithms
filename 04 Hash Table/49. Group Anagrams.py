class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()
    
# Time: O(N)
# Space: O(N)

# sorted: ['a', 'e', 't']
# sorted: ['a', 'e', 't']
# sorted: ['a', 'n', 't']
# sorted: ['a', 'e', 't']
# sorted: ['a', 'n', 't']
# sorted: ['a', 'b', 't']
# ans: defaultdict(<class 'list'>, {('a', 'e', 't'): ['eat', 'tea', 'ate'], ('a', 'n', 't'): ['tan', 'nat'], ('a', 'b', 't'): ['bat']})
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]    


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            ans[tuple(count)].append(s)

        return ans.values()

# Time: O(N)
# Space: O(N)

# defaultdict(<class 'list'>, {(1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['eat', 'tea', 'ate'], (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['tan', 'nat'], (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['bat']}) 

# dict_values([['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])