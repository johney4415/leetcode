from types import List, int


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]
        left = 0
        right = len(nums) - 1
        middle = (left + right) // 2
        while right >= left:
            if target > nums[middle]:
                left = middle + 1
            elif target < nums[middle]:
                right = middle - 1
            # else:

            middle = (left + right) // 2


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    target = 4
    ans = Solution().search(nums=nums, target=target)
    print(ans)
