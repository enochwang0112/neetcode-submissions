class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        def is_number(c):
            try:
                int(c)
                return True
            except ValueError:
                return False
        
        for token in tokens:
            if is_number(token):
                stack.append(int(token))
            else:
                lhs = stack.pop()
                rhs = stack.pop()
                if token == "+":
                    stack.append(lhs + rhs)
                elif token == "-":
                    stack.append(rhs - lhs)
                elif token == "*":
                    stack.append(lhs * rhs)
                else:
                    stack.append(int(rhs / lhs))
        
        return stack[0]