# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import List


class TwoSumII():
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        left = 0  # start of array, increments towards the start
        right = len(numbers) - 1
        sum = numbers[left] + numbers[right]
        while (left < right):
            if (sum < target):
                left += 1
            elif (sum > target):
                right -= 1
            sum = numbers[left] + numbers[right]
            if (sum == target):
                break
        return [left + 1, right + 1]
