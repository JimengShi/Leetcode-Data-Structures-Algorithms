# Let's define a function f(s) over a non-empty string s, which calculates the frequency of the smallest character 
# in s. For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2.

# Now, given string arrays queries and words, return an integer array answer, where each answer[i] is 
# the number of words such that f(queries[i]) < f(W), where W is a word in words.


# Example 1:
# Input: queries = ["cbd"], words = ["zaaaz"]
# Output: [1]
# Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").


# Example 2:
# Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
# Output: [1,2]
# Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").



class Solution:
	def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        # (1) define a function to compute frequency of the smallest character
		def frequency(s):
			t = sorted(list(s))[0]
			return s.count(t)
        
        # (2) use a list record frequency of queries and words
		query = [frequency(x) for x in queries]
		word = [frequency(x) for x in words]
        
        # (3) maintain an empty list and find the result
		res = []
		for x in query:
			count = 0
			for y in word:
				if y > x:
					count += 1
			res.append(count)
            
		return res
    
# s = "dcce"    
# list(s): convert string to list with each letter of string --> ['d', 'c', 'c', 'e']
# sorted(list(s)): sort the list ['d', 'c', 'c', 'e'] --> ['c', 'c', 'd', 'e']
# sorted(list(s))[0]: get the first element --> c
# s.count(t)