# Given a list accounts, each element accounts[i] is a list of strings, 
# where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is 
# some email that is common to both accounts. Note that even if two accounts have the same name, 
# they may belong to different people as people could have the same name. 
# A person can have any number of accounts initially, but all of their accounts definitely have the same name.

# After merging the accounts, return the accounts in the following format: the first element of each account is 
# the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

# Example 1: 
# Input: 
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], 
#             ["John", "johnnybravo@mail.com"], 
#             ["John", "johnsmith@mail.com", "john_newyork@mail.com"], 
#             ["Mary", "mary@mail.com"]]

# Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'], ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
# Explanation: 
# The first and third John's are the same person as they have the common email "johnsmith@mail.com".


# Method 1: dfs with recursion
from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # (0) pre-prepare: build an emails_accounts_map that maps an email to a list of accounts
        emails_accounts_map = defaultdict(list)
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]                           # get email starts from index 1
                emails_accounts_map[email].append(i)         # {'johnsmith@mail.com':[0, 2]}

        # (1) initialize the visited, result list
        visited = set()
        res = []
        
        # (2) DFS to traverse each account and look up map to find accounts with common email
        def dfs(i, emails):
            visited.add(i)
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]                       
                emails.add(email)                            
                for neighbor in emails_accounts_map[email]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        dfs(neighbor, emails)
        
        # (3) Perform DFS for each account to find an email maps how many accounts
        for i, account in enumerate(accounts):
            if i in visited:
                continue
            name = account[0]
            emails = set()
            dfs(i, emails)
            res.append([name] + sorted(emails))              # O(∑ai*logai)
        return res

# Time: O((∑ai*logai)), ai is the length of accounts[i]. Without the log factor, this is the complexity to build the graph and search for each component. The log factor is for sorting each component at the end.
# Space: O(∑ai), the space used by our graph and our search.
    
'''
[["John", "johnsmith@mail.com", "john00@mail.com"],          0
 ["John", "johnnybravo@mail.com"],                           1
 ["John", "johnsmith@mail.com", "john_newyork@mail.com"],    2
 ["Mary", "mary@mail.com"]]                                  3

{'john00@mail.com':         [0],
 'john_newyork@mail.com':   [2],
 'johnnybravo@mail.com':    [1],
 'johnsmith@mail.com':      [0, 2],
 'mary@mail.com':           [3]}

'''