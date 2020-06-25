class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        if len(s) == 2:
            if s[0]!= s[1]:
                return s[0]
        ans = {"position": 0, "max_len": 0}
        tmp_p = 0
        tmp_max = 0
        for i in range(len(s)):
            if ans['max_len'] > len(s)/2:
                print(s[ ans['position']: ans['max_len']+ans['position'] ])
                return s[ ans['position']: ans['max_len']+ans['position'] ]
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
                        if i == j or abs(i-j) == 1: 
                            ans['max_len'] = tmp_max
                            ans['position'] = i
                    if count + 1 > len(s):
                        break
                    if j < 0:
                        break

        result = s[ ans['position']: ans['max_len']+ans['position'] ]
        print(result)
        return result
if __name__ =="__main__":
    Solution.longestPalindrome(self="",s="joooohen")