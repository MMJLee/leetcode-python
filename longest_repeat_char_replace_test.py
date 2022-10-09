# https://leetcode.com/problems/longest-repeating-character-replacement/
from longest_repeat_char_replace import LongestRepeatCharReplace

tester = LongestRepeatCharReplace()


def test_general_case_one():
    assert tester.longest_repeat_char_replace("abab", 2) == 4


def test_replace_one():
    assert tester.longest_repeat_char_replace("aababba", 1) == 4


def test_no_replacements():
    assert tester.longest_repeat_char_replace("pwwkew", 0) == 2
