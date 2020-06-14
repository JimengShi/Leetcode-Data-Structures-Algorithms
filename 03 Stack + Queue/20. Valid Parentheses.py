class Solution:
    def isValid(self, s: str) -> bool:
        # (1) initialize a stack
        stack = []
        lookup = {"(" : ")", "[" : "]", "{" : "}"}
        
        # (2) traverse string
        for char in s:
            # case 1: append it on stack when we encounter left parenthese
            if char in lookup:
                stack.append(char)
                
            # case 2: check valid when we encounter right parenthese    
            elif len(stack) == 0 or lookup[stack.pop()] != char:     # stack.pop() means the last one that was inserted lookup
                return False
        
        # (3) to see if stack is empty when we finish traversing the string
        return len(stack) == 0

# Time: O(n) because we traverse the given string one character once and push and pop operations on a stack take O(1) time.
# Space: O(n) as we push all opening brackets onto the stack and in the worst case, we will end up pushing all the brackets onto the stack. e.g. ((((((((((.

   
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if (c == ')' and stack[-1] == '(') or (c == ']' and stack[-1] == '[') or (c == '}' and stack[-1] == '{'):
                    stack.pop()
                else:
                    return False
                
        return len(stack) == 0
    
# Time: O(n) because we simply traverse the given string one character once and push and pop operations on a stack take O(1) time.
# Space: O(n) as we push all opening brackets onto the stack and in the worst case, we will end up pushing all the brackets onto the stack. e.g. ((((((((((.