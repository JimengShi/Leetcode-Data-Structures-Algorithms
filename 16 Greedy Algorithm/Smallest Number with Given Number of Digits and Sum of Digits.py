# Problem
# How to find the smallest number with given digit sum s and number of digits m?
# Input : s = 9, m = 2
# Output : 18
# There are many other possible numbers like 45, 54, 90, etc with sum of digits as 9 and number of digits as 2. The smallest of them is 18.

# Input : s = 20, m = 3
# Output : 299


def findSmallest(m, s):
    # (0) edge case
    if s == 0:
        if m == 1:
              print("Smallest number is 0") 
        else: 
              print("Not possible")
        return
    
    if s > 9*m:
        print("Not possible")
        return

    # (1) deduct sum by one to account for cases later (There must be 1 left for the most significant (leftmost) digit)
    s -= 1
    
    # (2) initialize an array to save result
    res = [0 for i in range(m)]
    
    # (3) greedy: from the right to left, trying big value 9, and lower
    for i in range(m-1, 0, -1):
        if (s > 9):              # sum > 9, last digit == 9
            res[i] = 9
            s -= 9
        else:
            res[i] = s           # sum < 9, last digit == s
            s = 0
    res[0] = s + 1               # the leftmost digit = s+1

    # (3) Method 1 to return result
    print("Smallest number is ", end='')
    for i in range(m):
        print(res[i], end='')

    # (3) Method 2 to return result
    ans = 0
    for i in range(m):
        ans = ans * 10 + res[i]
    return ans

# Time: O(N)
# Space: O(N)