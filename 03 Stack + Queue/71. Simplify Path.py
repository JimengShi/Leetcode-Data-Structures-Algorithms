class Solution:
    def simplifyPath(self, path: str) -> str:
        lst = []
        splits = path.split("/")   # ['', 'a', '.', 'b', '..', '..', 'c', 'd', '..', 'e', 'f', 'g', '..', '']

        for s in splits:
            if s == "":
                continue
            if s == ".":
                continue
            if s == "..":
                if len(lst) != 0:
                    lst.pop()
            else:
                lst.append(s)

        result = []
        if len(lst) == 0:
            return "/"
        result = ['/' + i for i in lst]
        return ''.join(result)
    
# Time: O(N). We spend O(N) to split the input path and O(N) to traverse each component one by one again.
# Space: O(N). O(N) for split and O(N) for stack.