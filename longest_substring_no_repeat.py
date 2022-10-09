# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class LongestSubstringNoRepeat():
    def longest_substring_no_repeat(self, str: str) -> int:
        charSet = set()  # {} is dict
        max_length = 0
        left = 0
        for curr in range(len(str)):
            # repeat (removing char at left index and incrementing) until val at curr index is not in set
            while str[curr] in charSet:
                charSet.remove(str[left])
                left += 1
            charSet.add(str[curr])
            max_length = max(max_length, curr - left + 1)
        return max_length
