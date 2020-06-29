class Solution:
    def letterCombinations(self, digits):
        if digits == "":
            return [] 
        word = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        '''
        if 
        word = {'2': "abc",'3': "def",'4': "ghi",'5': "jkl",'6': "mno",'7': "pqrs",'8': "tuv",'9': "wxyz"}
        can faster
        '''
        res = ['']
        for e in digits:
            res = [w + c for c in word[e] for w in res]
        return res

if __name__ == "__main__":
    digits = '233'
    ans = Solution().letterCombinations(digits=digits)
    print(ans)

