# https://leetcode.com/problems/group-anagrams/

from collections import defaultdict
from typing import List


class GroupAnagrams():
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)  # mapping charCount to list of anagrams
        for word in strs:
            count = [0] * 26  # a to z

            for char in word:
                # getting indices 0 - 26 corresponding to a - z through the ord() method
                count[ord(char) - ord("a")] += 1
            ans[tuple(count)].append(word)
        return list(ans.values())
