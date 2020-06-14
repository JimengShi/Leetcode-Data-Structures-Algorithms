# Time: O(∑ai*logai), where ai is the length of accounts[i]. Without the log factor, this is the complexity to build the graph and search for each component. The log factor is for sorting each component at the end.
# Space: O(∑ai), the space used by our graph and our search.

# Method 1: dfs with recursion
from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # (0) initialize the visited, result list and emails_accounts_map
        visited = [False] * len(accounts)
        emails_accounts_map = defaultdict(list)
        res = []
        
        # (1) build an emails_accounts_map that maps an email to a list of accounts
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]                           # get email starts from 2nd
                emails_accounts_map[email].append(i)         # {'johnsmith@mail.com':[0, 2]}
        
        # (2) DFS to traverse each account and look up map to find accounts with common email
        def dfs(i, emails):
            if visited[i]:
                return
            visited[i] = True
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]                       
                emails.add(email)                            
                for neighbor in emails_accounts_map[email]:
                    dfs(neighbor, emails)
        
        # (3) Perform DFS for each account to find an email maps how many accounts
        for i, account in enumerate(accounts):
            if visited[i]:
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


# Method 2: dfs with stack
class Solution(object):
    def accountsMerge(self, accounts):
        em_to_name = {}
        graph = collections.defaultdict(set)
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
                em_to_name[email] = name

        seen = set()
        ans = []
        for email in graph:
            if email not in seen:
                seen.add(email)
                stack = [email]
                component = []
                while stack:
                    node = stack.pop()
                    component.append(node)
                    for nei in graph[node]:
                        if nei not in seen:
                            seen.add(nei)
                            stack.append(nei)
                ans.append([em_to_name[email]] + sorted(component))
        return ans
    
# Time: O((∑ai*logai)), ai is the length of accounts[i]. Without the log factor, this is the complexity to build the graph and search for each component. The log factor is for sorting each component at the end.
# Space: O(∑ai), the space used by our graph and our search.