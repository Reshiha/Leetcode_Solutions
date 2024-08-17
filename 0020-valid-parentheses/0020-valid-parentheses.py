class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_map = {'(':')', '{':'}','[':']'}
        for char in s:
            if char in hash_map:
                stack.append(char)
            elif stack and hash_map[stack[-1]] == char:
                stack.pop()
            else:
                return False
        return not stack
        