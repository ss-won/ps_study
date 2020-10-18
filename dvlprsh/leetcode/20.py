def isPair(left, right):
    if left == '(' and right == ')':
        return True
    elif left == '{' and right == '}':
        return True
    elif left == '[' and right == ']':
        return True
    else:
        return False

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for v in s:
            if not stack:
                stack.append(v)
                continue
            if isPair(stack[-1], v):
                stack.pop()
            else:
                stack.append(v)

        if stack:
            return False
        else:
            return True