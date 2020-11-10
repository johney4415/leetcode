class Solution:
    def search(self, nums, target):
        total_len = len(nums)
        if total_len == 0:
            return -1
        if total_len == 1:
            if nums[0] == target:
                return 0
            return -1
        if total_len == 2:
            if nums[0] == target:
                return 0
            elif nums[1] == target:
                return 1
            else:
                return -1
        if nums[total_len // 2] == target:
            return total_len // 2
        if nums[total_len // 2] <= nums[total_len - 1]:  #右邊有序
            if target >= nums[total_len // 2] and target <= nums[total_len -
                                                                 1]:
                pointer = total_len // 2
                while nums[pointer] <= target:
                    if nums[pointer] == target:
                        return pointer
                    pointer += 1
                return -1
            else:
                if target < nums[0]:
                    pointer = total_len // 2
                    while nums[pointer] >= target:
                        if nums[pointer] == target:
                            return pointer
                        pointer -= 1
                        if pointer < 0:
                            return -1
                    return -1
                else:
                    pointer = 0
                    while nums[pointer] <= target:
                        if nums[pointer] == target:
                            return pointer
                        pointer += 1
                        if pointer >= total_len:
                            return -1
                    return -1

        else:  #左邊有序
            if target <= nums[total_len // 2] and target >= nums[0]:
                pointer = 0
                while target >= nums[pointer]:
                    if target == nums[pointer]:
                        return pointer
                    pointer += 1
                return -1
            else:
                if target <= nums[0]:  # 最右到中間
                    pointer = total_len - 1
                    while nums[pointer] >= target:
                        if nums[pointer] == target:
                            return pointer
                        pointer -= 1
                        if pointer == 0:
                            return -1
                    return -1
                else:  # 中間到最右
                    pointer = total_len // 2
                    while target >= nums[pointer]:
                        if nums[pointer] == target:
                            return pointer
                        pointer += 1
                        if pointer >= total_len:
                            return -1
                    return -1


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    target = 4
    ans = Solution().search(nums=nums, target=target)
    print(ans)
