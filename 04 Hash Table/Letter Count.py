# Method 1: hash table - dictionary
def letterCount(s):
    # (1) build dictionary to count frequency
    freq = {}
    for piece in s:
        for c in piece:
            if c.isalpha():
                freq[c] = 1 + freq.get(c, 0)         # default 0
    print(freq)
    
    # (2) find the most frequent letter
    max_word = ''
    max_count = 0
    for (w, c) in freq.items():                      # (key, value) tuples represent (word, count)
        if c > max_count:
            max_word = w
            max_count = c
    
    print('The most frequent word is', max_word)
    print('Its number of occurrences is', max_count)  


# s = "Hello World How are you I am fine thank you and you"
# letterCount(s)
# {'H': 2, 'e': 3, 'l': 3, 'o': 6, 'W': 1, 'r': 2, 'd': 2, 'w': 1, 'a': 4, 'y': 3, 'u': 3, 'I': 1, 'm': 1, 'f': 1, 'i': 1, 'n': 3, 't': 1, 'h': 1, 'k': 1}
# The most frequent word is o
# Its number of occurrences is 6


# Method 2: Counter
from collections import Counter
def letterCount2(s):
    c = Counter(x for x in s if x != " ")
    
    print(c, '\n')
    print(c.most_common(), '\n')
    
    for letter, count in c.most_common(4):
        print('%s: %5d' % (letter, count))    # 5 here means 5 spaces

# Counter({'o': 6, 'a': 4, 'e': 3, 'l': 3, 'y': 3, 'u': 3, 'n': 3, 'H': 2, 'r': 2, 'd': 2, 'W': 1, 'w': 1, 'I': 1, 'm': 1, 'f': 1, 'i': 1, 't': 1, 'h': 1, 'k': 1}) 
# [('o', 6), ('a', 4), ('e', 3), ('l', 3), ('y', 3), ('u', 3), ('n', 3), ('H', 2), ('r', 2), ('d', 2), ('W', 1), ('w', 1), ('I', 1), ('m', 1), ('f', 1), ('i', 1), ('t', 1), ('h', 1), ('k', 1)]
# o:     6
# a:     4
# e:     3
# l:     3