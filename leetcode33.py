class Solution:
    def search(self, nums, target):
        total_len = len(nums)
        if total_len ==1:
            if nums[0] == target:
                return 0
            else:
                return -1
        i = int(total_len/2)
        if total_len %2 == 0:
            # 偶數
            # nums[i] < 
        else:
            # 基數
                