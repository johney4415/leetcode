class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i - 1]:
                continue
            d = {}
            for x in nums[i + 1:]:
                if x not in d:
                    d[-v - x] = 0
                else:
                    res.add((v, -v - x, x))
        return list(res)


if __name__ == "__main__":
    nums = [-4, -2, 1, -5, -4, -4, -2, 0, 4, 0, -2, 3]
    ans = Solution().threeSum(nums=nums)
    print(ans)