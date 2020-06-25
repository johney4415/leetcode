class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        if len(s) == 2:
            if s[0] != s[1]:
                return s[0]
        ans = {"position": 0, "max_len": 0}
        tmp_p = 0
        tmp_max = 0
        for i in range(len(s)):
            if ans['max_len'] > len(s) / 2:
                print(s[ans['position']:ans['max_len'] + ans['position']])
                return s[ans['position']:ans['max_len'] + ans['position']]
            for j in range(len(s) - 1, -1, -1):
                # print(s[i],s[j])
                count = i
                if count >= len(s):
                    break
                if i > j or j < 0:
                    break
                tmp_max = 0
                if j < 0:
                    break
                while s[count] == s[j]:
                    count += 1
                    j -= 1
                    tmp_max += 1
                    tmp_p = i
                    if tmp_max > ans['max_len']:
                        if i == j or abs(i - j) == 1:
                            ans['max_len'] = tmp_max
                            ans['position'] = i
                    if count + 1 > len(s):
                        break
                    if j < 0:
                        break

        result = s[ans['position']:ans['max_len'] + ans['position']]
        print(result)
        return result


class Solution4(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return None
        if len(s) < 2:
            return s
        T = '#'.join('@{}$'.format(s))  #step 1
        #step2
        n = len(T)
        P = [0] * n
        c = 0
        r = 0
        for i in range(1, n - 1):
            i_mirror = c - (i - c)  #i关于中心c的对称位置
            if r > i:  #利用之前回文串字符对比重复部分
                P[i] = min(r - i, P[i_mirror])
            # 中心扩展法完成之前没有涉及的字符比对
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] = P[i] + 1
            #更新当前回文串中心c及终止位置r
            if i + P[i] > r:
                c = i
                r = i + P[i]
        #找到最大回文半径及对应的回文中心
        maxlen = 0
        centeridx = 0
        for i in range(1, n - 1):
            if P[i] > maxlen:
                maxlen = P[i]
                centeridx = i
        #获取最长回文串
        begin = (centeridx - maxlen) // 2
        end = (centeridx + maxlen) // 2
        return s[begin:end]


if __name__ == "__main__":
    Solution.longestPalindrome(self="", s="joooohen")
