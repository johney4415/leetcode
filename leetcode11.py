class Solution:
    def maxArea(self, height):
        if not height:
            return 0
        max_value = 0
        right = len(height) - 1
        left = 0
        while right > left:
            if height[right] > height[left]:
                tmp_value = (right - left) * height[left]
                left += 1
            else:
                tmp_value = (right - left) * height[right]
                right -= 1
            if tmp_value > max_value:
                max_value = tmp_value
        return max_value


if __name__ == "__main__":
    li = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    Solution().maxArea(li)