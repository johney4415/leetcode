class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if not str:
            return 0

        flag = True
        ans = 0
        if str[0] == "-":
            flag = False
            str = str[1:]
        elif str[0] == "+":
            str = str[1:]
        for i in str:
            try:
                int(i)
                ans = ans * 10 + int(i)
            except:
                break
        ans = ans * -1 if not flag else ans
        ans = ans if ans <= 2147483647 else 2147483647
        ans = ans if ans >= -2147483648 else -2147483648
        print(ans)
        return ans


if __name__ == "__main__":
    Solution().myAtoi(str="+46")