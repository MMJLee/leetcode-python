# https://leetcode.com/problems/combination-sum/
from typing import List


class CombinationSum:
    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, subset, total):
            # if subset_total = target, add to res list and break recursion
            if total == target:
                res.append(subset.copy())
                return
            # if subset_total > target or index out of bounds, break recursion
            if total > target or i >= len(candidates):
                return
            subset.append(candidates[i])
            # tree to include cur value
            dfs(i, subset, total + candidates[i])
            subset.pop()
            # tree to exclude cur value
            dfs(i+1, subset, total)
        dfs(0, [], 0)
        return res
