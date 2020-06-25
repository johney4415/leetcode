#  palindrome_number
import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        try:
            x = int(x)
        except:
            return False
        if x < 0:
            return False
        if x == 0 or x < 10:
            return True
        lenth = int(math.log10(x)) + 1
        x = str(x)
        if lenth % 2 == 0:
            mid_number = int(lenth / 2) - 1
            pos = mid_number + 1
            neg = mid_number
            while x[pos] == x[neg]:
                if neg == 0:
                    return True
                pos += 1
                neg -= 1
        else:
            # 奇數
            mid_number = int((lenth + 1) / 2) - 1
            pos = mid_number
            neg = mid_number
            while x[pos] == x[neg]:
                if neg == 0:
                    return True
                pos += 1
                neg -= 1
        return False


if __name__ == "__main__":
    a = Solution().isPalindrome(x=11)
    print(a)