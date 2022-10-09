# https://leetcode.com/problems/longest-substring-without-repeating-characters/

from longest_substring_no_repeat import LongestSubstringNoRepeat

tester = LongestSubstringNoRepeat()


def test_general_case():
    assert tester.longest_substring_no_repeat("abcabcbb") == 3


def test_single_letter():
    assert tester.longest_substring_no_repeat("bbbbb") == 1


def test_advance_left_by_two():
    assert tester.longest_substring_no_repeat("pwwkew") == 3
