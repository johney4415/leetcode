from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        tmp_sum = nums[0]
        for i in range(1, len(nums)):
            tmp_sum = max(tmp_sum + nums[i], nums[i])
            max_sum = max(max_sum, tmp_sum)
        return max_sum


if __name__ == "__main__":
    nums = [1, 2]
    ans = Solution().maxSubArray(nums=nums)
    print(ans)
