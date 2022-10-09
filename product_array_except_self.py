# https://leetcode.com/problems/product-of-array-except-self/
from typing import List


class ProductArrayExceptSelf():
    def product_array_except_self(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        leftProd = 1  # products of array from the left side
        for i in range(len(nums)):
            res[i] = leftProd
            leftProd *= nums[i]
        rightProd = 1  # products of array from the right side
        for i in range(len(nums)-1, -1, -1):
            res[i] *= rightProd
            rightProd *= nums[i]
        return res

# (1, 2, 3, 4) - input array
# (1, 1, 2, 6) - left array
# (24, 12, 4, 1) - right array
# (24, 12, 8, 6) - output array
