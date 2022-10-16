# https://leetcode.com/problems/permutations/
from typing import List


# not sure why single test case does not work. Need to investigate
class Permutations():
    def permutations(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs():
            if (len(subset) == len(nums)):
                res.append(subset.copy())
                return
            for i in range(len(nums)):
                if nums[i] not in subset:
                    subset.append(nums[i])
                    dfs()
                    subset.pop()
        return res
