# sort the words, then keep in the set and check for nextWord[:-1] in the set
class Solution:
    def longestWord(self, words: List[str]) -> str:        
        words.sort()
        res = ""
        st = set()
        st.add("")
        
        for word in words:
            if word[:-1] in st:
                st.add(word)
                if len(word) > len(res):
                    res = word

        return res
    
# Time: O(sum(w)+N), w is the length of each word in words, N is the length of words.
# Space: O(sum(w))
    
    
# sorted words: ['a', 'ap', 'app', 'appl', 'apple', 'apply', 'banana'] 

# word: a
# res: a
# set: {'', 'a'}
# ----------
# word: ap
# res: ap
# set: {'', 'a', 'ap'}
# ----------
# word: app
# res: app
# set: {'', 'a', 'app', 'ap'}
# ----------
# word: appl
# res: appl
# set: {'', 'appl', 'app', 'ap', 'a'}
# ----------
# word: apple
# res: apple
# set: {'', 'appl', 'app', 'ap', 'apple', 'a'}
# ----------
# word: apply
# res: apple
# set: {'', 'appl', 'app', 'ap', 'apply', 'apple', 'a'}
# ----------
# word: banana