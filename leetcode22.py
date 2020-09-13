# Generate Parentheses


class Solution:
    def generateParenthesis(self, n: int):
        if n == 0:
            return []
        result = []
        self.helper(n, n, '', result)
        return result

    def helper(self, l, r, item, result):
        if r < l:
            return None
        if l == 0 and r == 0:
            result.append(item)
        if l > 0:
            self.helper(l - 1, r, item + '(', result)
        if r > 0:
            self.helper(l, r - 1, item + ')', result)
