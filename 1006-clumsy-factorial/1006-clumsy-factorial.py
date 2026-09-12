class Solution(object):
    def clumsy(self, n):
        stack = [n]
        n -= 1
        op = 0

        while n > 0:
            if op == 0:
                stack[-1] *= n
            elif op == 1:
                top=stack[-1]
                stack[-1] = -(-top//n) if top<0 else top//n
                
            elif op == 2:
                stack.append(n)
            else:
                stack.append(-n)

            op = (op + 1) % 4
            n -= 1

        return sum(stack)
        