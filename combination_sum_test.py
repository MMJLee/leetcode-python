# https://leetcode.com/problems/combination-sum/

from combination_sum import CombinationSum

tester = CombinationSum()


def test_general_case_one():
    assert tester.combination_sum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]


def test_general_case_two():
    assert tester.combination_sum([2, 3, 5], 8) == [
        [2, 2, 2, 2], [2, 3, 3], [3, 5]]


def test_single_case():
    assert tester.combination_sum([2], 1) == []
