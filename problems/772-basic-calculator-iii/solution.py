class Solution:
    def calculate(self, s: str) -> int:
        stack = collections.deque()
        operand = 0
        sign = "+"
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                operand = (operand) * 10 + int(c)
            elif c == "(": # recursion
                cnt = 0
                j = i
                while i < len(s):
                    if s[i] == "(": cnt += 1
                    if s[i] == ")": cnt -= 1
                    if cnt == 0: break
                    i += 1
                operand = self.calculate(s[j+1:i]) # skip i here
              
            if (not c.isdigit() and not c.isspace()) or i == len(s)-1:
                if sign == '+':
                    stack.append(operand)
                if sign == "-":
                    stack.append(-operand)
                if sign == "*":
                    stack.append(stack.pop() * operand)
                if sign == "/":
                    t = stack.pop()
                    if t // operand < 0 and t % operand != 0:
                        stack.append(t // operand + 1)
                    else:
                        stack.append(t // operand)
                    operand = 0
                sign = c
                operand = 0 
            i += 1
    
        return sum(stack)