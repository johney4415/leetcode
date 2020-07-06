class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            else:
                if c in ['(', '[', '{']:
                    stack.append(c)
                else:
                    remove_c = stack.pop()
                    if remove_c == '(' and c != ')' or remove_c == '[' and c != ']' or remove_c == '{' and c != '}':
                        return False
        if not stack:
            return True


if __name__ == "__main__":
    str_test = "[]"
    ans = Solution().isValid(s=str_test)
    print(ans)
