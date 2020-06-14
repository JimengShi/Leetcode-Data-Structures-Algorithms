from collections import Counter
def wordCount(s):
    splits = s.split()
    print(s.split())
    
    freq = {}
    for sp in splits:
        freq[sp] = 1 + freq.get(sp, 0)
    print(freq)

    word = ''
    max_count = 0
    for key, val in freq.items():
        if val > max_count:
            word = key
            max_count = val
    return (word, max_count)

# s = "Hello World How are you I am fine thank you and you"
# wordCount(s)

# ['Hello', 'World', 'How', 'are', 'you', 'I', 'am', 'fine', 'thank', 'you', 'and', 'you']
# {'Hello': 1, 'World': 1, 'How': 1, 'are': 1, 'you': 3, 'I': 1, 'am': 1, 'fine': 1, 'thank': 1, 'and': 1}
# ('you', 3)


from collections import Counter
def wordCount(s):
    wordcount = Counter(s.split())
    print(s.split())
    print(wordcount)

# s = "Hello World How are you I am fine thank you and you"
# wordCount(s)
# ['Hello', 'World', 'How', 'are', 'you', 'I', 'am', 'fine', 'thank', 'you', 'and', 'you']
# Counter({'you': 3, 'Hello': 1, 'World': 1, 'How': 1, 'are': 1, 'I': 1, 'am': 1, 'fine': 1, 'thank': 1, 'and': 1})



def split(s):
    ans = []
    res = ''
    for word in s:
        for letter in word:
            if letter.isalpha():
                res += letter
            else:
                ans.append(res)
                res += ','
                res = ''
    print(ans)


# s = "Hello World How are you I am fine thank you and you"
# split(s)
# ['Hello', 'World', 'How', 'are', 'you', 'I', 'am', 'fine', 'thank', 'you', 'and']