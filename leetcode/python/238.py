from typing import List


class Solution(object):
    def product_except_self(self, nums: List[int]) -> List[int]:
        left, right = [], []
        left_product, right_product = 1, 1
        for i, _ in enumerate(nums):
            if i > 0:
                left_product *= nums[i - 1]
            if 0 < i < len(nums):
                right_product *= nums[len(nums) - i]
            right.append(right_product)
            left.append(left_product)
        ans = []
        for i, _ in enumerate(nums):
            ans.append(left[i] * right[len(nums) - i - 1])
        return ans

if __name__ == '__main__':
    s = Solution()
    arr = [1,2,3,4]
    print(s.product_except_self(nums=arr))
