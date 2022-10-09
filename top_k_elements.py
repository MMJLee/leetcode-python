#https://leetcode.com/problems/top-k-frequent-elements/
from typing import List


class TopKElements():
    def top_k_elements(self, nums: List[int], k: int) -> List[int]:
        count = {}  # num as key, freq as value
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        # max freq is length of nums. freq as key, list(num) as value
        freqArray = [[] for i in range(len(nums) + 1)]
        for num, freq in count.items():
            freqArray[freq].append(num)
        res = []
        # iterate backwards
        for i in range(len(freqArray) - 1, 0, -1):
            for n in freqArray[i]:
                res.append(n)
                if len(res) == k:
                    return res
