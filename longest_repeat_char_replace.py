# https://leetcode.com/problems/longest-repeating-character-replacement/

class LongestRepeatCharReplace():
    def longest_repeat_char_replace(self, str: str, k: int) -> int:
        count = {}
        res = 0
        left = 0
        maxF = 0
        # basically trying to find the longest repeating substring but k values can be different
        for right in range(len(str)):
            # dict counting freq of characters
            count[str[right]] = 1 + count.get(str[right], 0)
            maxF = max(maxF, count[str[right]])
            # (right - left + 1) - maxF is the # of characters that need to be replaced
            while (right - left + 1) - maxF > k:
                # start decrementing frequencies of characters as left index starts moving
                count[str[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
