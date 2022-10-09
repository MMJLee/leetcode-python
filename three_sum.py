# https://leetcode.com/problems/3sum/
# basically a two sum II with an added step
from typing import List


class ThreeSum():
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for index, val in enumerate(nums):
            if (index > 0 and val == nums[index-1]):
                continue
            left, right = index + 1, len(nums) - 1
            while (left < right):
                sum = val + nums[left] + nums[right]
                if (sum > 0):
                    right -= 1
                elif (sum < 0):
                    left += 1
                else:
                    res.append([val, nums[left], nums[right]])
                    left += 1
                    while (nums[left] == nums[left - 1] and left < right):
                        left += 1
        return res
