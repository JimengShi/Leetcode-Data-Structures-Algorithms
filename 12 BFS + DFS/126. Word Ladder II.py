from collections import defaultdict
import string
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # (0) edge case
        if endWord not in wordList: 
            return []
        
        # (1) initialize data structure
        dic = set(wordList)
        level = {beginWord}
        parents = defaultdict(set)
        
        # (2) bfs
        while level and endWord not in parents:
            next_level = defaultdict(set)
            for node in level:
                for char in string.ascii_lowercase:             # for char in 'abcdefghijklmnopqrstuvwxyz':
                    for i in range(len(beginWord)):
                        temp = node[:i] + char + node[i+1:]
                        if temp in dic and temp not in parents:
                            next_level[temp].add(node)
            level = next_level
            parents.update(next_level)
            
        # (3) save path from parent    
        res = [[endWord]]
        while res and res[0][0] != beginWord:
            res = [[p]+r for r in res for p in parents[r[0]]]
        return res

    
# node: hit
# temp: hot
# next_level: defaultdict(<class 'set'>, {'hot': {'hit'}})
# parent: defaultdict(<class 'set'>, {'hot': {'hit'}})
# -------------
# node: hot
# temp: dot
# next_level: defaultdict(<class 'set'>, {'dot': {'hot'}})
# temp: lot
# next_level: defaultdict(<class 'set'>, {'dot': {'hot'}, 'lot': {'hot'}})
# parent: defaultdict(<class 'set'>, {'hot': {'hit'}, 'dot': {'hot'}, 'lot': {'hot'}})
# -------------
# node: dot
# temp: dog
# next_level: defaultdict(<class 'set'>, {'dog': {'dot'}})
# node: lot
# temp: log
# next_level: defaultdict(<class 'set'>, {'dog': {'dot'}, 'log': {'lot'}})
# parent: defaultdict(<class 'set'>, {'hot': {'hit'}, 'dot': {'hot'}, 'lot': {'hot'}, 'dog': {'dot'}, 'log': {'lot'}})
# -------------
# node: dog
# temp: cog
# next_level: defaultdict(<class 'set'>, {'cog': {'dog'}})
# node: log
# temp: cog
# next_level: defaultdict(<class 'set'>, {'cog': {'dog', 'log'}})
# parent: defaultdict(<class 'set'>, {'hot': {'hit'}, 'dot': {'hot'}, 'lot': {'hot'}, 'dog': {'dot'}, 'log': {'lot'}, 'cog': {'dog', 'log'}})
# -------------
# [['cog']]
# [['dog', 'cog'], ['log', 'cog']]
# [['dot', 'dog', 'cog'], ['lot', 'log', 'cog']]
# [['hot', 'dot', 'dog', 'cog'], ['hot', 'lot', 'log', 'cog']]
# [['hit', 'hot', 'dot', 'dog', 'cog'], ['hit', 'hot', 'lot', 'log', 'cog']]