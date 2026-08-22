class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # loop through tokens
        # if token is a number, append to stack
        # if token is an operation, pop top 2 values in stack, carry out the operation. Push result onto stack
        
        stack = []

        for token in tokens:
            if token not in {'+', '-', '*', '/'}:
                stack.append(int(token))
            else: # is an operator
                # get operands
                num2 = stack.pop()
                num1 = stack.pop()
                if token == '+':
                    stack.append(num1 + num2)
                elif token == '-':
                    stack.append(num1 - num2)
                elif token == '*':
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num1/num2))
                
        return stack[-1]