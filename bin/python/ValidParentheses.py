class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if c == ')' and stack[-1] != '(':
                    return False
                if c == '}' and stack[-1] != '{':
                    return False
                if c == ']' and stack[-1] != '[':
                    return False
                stack.pop()

        return len(stack) == 0

    def isValid2(self, s: str) -> bool:
        clos = {')': '(', '}': '{', ']': '['}

        stack = []

        for c in s:
            if c not in clos:
                stack.append(c)
                continue
            if not stack or clos[c] != stack.pop():
                return False

        return not stack

    def isValid3(self, s: str) -> bool:
        prev = None
        while prev != s:
            prev = s
            s = s.replace("()", "").replace("[]", "").replace("{}", "")
        return not prev


solution = Solution()
print(solution.isValid("{}"))
print(solution.isValid2("{[()]}"))
print(solution.isValid3("{[()]}"))
