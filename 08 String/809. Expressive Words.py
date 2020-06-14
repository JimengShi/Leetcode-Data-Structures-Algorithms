# Algorithm:

# (1) firstly use the process function to get the characters that appear without repeating in the string and frequencies. For example: string "helloo", chars=['h','e','l','o'] and counts = [1,1,2,2].

# (2) If given more investigation when any of the strings in the words list has the same characters as S, since characters are the same, we need to figure out if word can be extended to S based on the expansion rules.

# (3) If frequency of characters are the same or if we need to expand the character in word == frequency with the same character in S, the final frequency of the character will be 3 or more, then it is expandable. 

# (4) If all of the characters in the word are expandable according to this rule, we have a word that can be changed to S, so we only need to return the number of these words.

class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        # (1) get the characters and corresponding frequencies in the string
        # For example: string "helloo", chars = ['h','e','l','o'] and counts = [1,1,2,2]
        def process(st):
            if not st:
                return [], []
            
            chars, counts = [st[0]], [1]
            for i in range(1, len(st)):
                if st[i] == chars[-1]:        # repeating character
                    counts[-1] += 1
                else:                         # new character
                    chars.append(st[i])
                    counts.append(1)
            return chars, counts
                
        
        ans = 0
        s_chars, s_counts = process(S)
        for word in words:
            w_chars, w_counts = process(word)
            # basic conditon to expand
            if s_chars == w_chars:
                counter = 0
                for k in range(len(w_chars)):
                    # expandable rule  
                    # w_counts[k] == s_counts[k]
                    # to expand the word whose characters is same as characters in S, the frequency should >= 3
                    if w_counts[k] == s_counts[k] or (w_counts[k] < s_counts[k] and s_counts[k] >= 3):
                        counter += 1
                
                if counter == len(s_chars):
                    ans += 1

        return ans


from collections import Counter
class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        ans = 0
        
        s_counter = Counter(S)                          # "heeellooo" --> {'h':1, 'e':3, 'l':2, 'o':3}    
        for word in words:                              # words = ["hello", "hi", "helo"]
            w_counter = Counter(word)                   # w_counter = {'h':1, 'e':1, 'l':2, 'o':1} for word = "hello"
            
            if w_counter.keys() == s_counter.keys():    
                count = 0
                for key in w_counter.keys():
                    if w_counter[key] == s_counter[key] or (w_counter[key] < s_counter[key] and s_counter[key] >= 3):
                        count += 1
                
                if count == len(s_counter):
                    ans += 1

        return ans
    
    
# Time: O(mn), O(n) for Counter(S), O(m) for traversing words, O(n) for Counter(word)
# Space: O(n+m) for dictionary to save S and word