from collections import Counter
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # (1) initialize dictionary
        ans = collections.Counter()
        
        # (2) split each sample in given array
        for domain in cpdomains:             # domain = "900 google.mail.com"
            count, domain = domain.split()   # count = '900', domain = 'google.mail.com'
            count = int(count)               # count = 900
            frags = domain.split('.')        # frags = ['google', 'mail', 'com']
            
            for i in range(len(frags)):
                ans[".".join(frags[i:])] += count
        
        # (3) return result with format
        return ["{} {}".format(ct, dom) for dom, ct in ans.items()]

    
# Time: O(N), where N is the length of cpdomains, and assuming the length of cpdomains[i] is fixed.
# Space: O(N), the space used in our count.


# string_name.join(iterable) 
# string_name: It is the name of string in which joined elements of iterable will be stored.
# list1 = ['1','2','3','4']  
# s = '-'.join(list1)        # joins elements of list1 by '-' and stores in sting s 
# print(s)                   # join use to join a list of strings to a separator s 