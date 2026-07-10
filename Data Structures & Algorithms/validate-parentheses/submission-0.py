class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {'()', '{}', '[]'}

        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if not stack or stack[-1] + c not in valid:
                    return False
                stack.pop()
        
        return not stack

        