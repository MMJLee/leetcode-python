# https://leetcode.com/problems/group-anagrams/

from group_anagrams import GroupAnagrams

tester = GroupAnagrams()


def test_general_case():
    assert tester.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]).sort() == [
        ["eat", "tea", "ate"], ["tan", "nat"], ["bat"]].sort()


def test_empty_case():
    assert tester.group_anagrams([]).sort() == [[]].sort()


def test_single_list_anagrams():
    assert tester.group_anagrams(["eat", "tea", "ate"]).sort() == [
        ["eat", "tea", "ate"]].sort()


def test_single_word():
    assert tester.group_anagrams(["eat"]).sort() == [
        ["eat"]].sort()
