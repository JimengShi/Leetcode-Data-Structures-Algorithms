# running time: O(m*n^2), n = len(s), m = len(wordDict)
# Let‘s say the average word length in wordDict is k, so it takes n/k times to reach end.
# Each time, the helper function would be called and it's running time is O(m*n)
# So the whole runinng time would be O(m*n*n/k), which is O(m*n^2)
class Solution(object):
    def wordBreak(self, s, wordDict):
        dic = collections.defaultdict(list)

        def helper(s):
            if not s: 
                return [None]
            if s in dic: 
                return dic[s]
            
            res = []
            for word in wordDict:
                n = len(word)
                if word == s[:n]:
                    # result from the rest of string s  -->  s[n:]
                    for each in helper(s[n:]):
                        if each:
                            res.append(word + " " + each)
                        else:
                            res.append(word)
                dic[s] = res
            return res

        return helper(s)
