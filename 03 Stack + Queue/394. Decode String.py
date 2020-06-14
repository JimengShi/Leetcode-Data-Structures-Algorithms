# four situations: 
# 1. integer
# 2. letter
# 3. left square bracket 
# 4. right square bracket 

class Solution:
    def decodeString(self, s: str) -> str:
		# (0) edge case
        if not s:
            return s
        
        # (1) initialize stack and num
        stack = []
        stack.append(["", 1])
        num = ""

        # (2) traverse string
        for ch in s:
            if ch.isdigit():                  # case 1: make sure num when encounter digits
                num += ch
            elif ch == '[':                   # case 3: append num when encounter '['
                stack.append(["", int(num)])
                num = ""
            elif ch == ']':                   # case 4: append string between '[' and ']' when encounter ']'
                st, k = stack.pop()
                stack[-1][0] += st*k
            else:                             # case 2: append char when encounter char
                stack[-1][0] += ch

        # (3) return result
        return stack[0][0]
    
# Time: O(N)
# Space: O(N)