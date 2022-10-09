# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from two_sum_II import TwoSumII

tester = TwoSumII()


def test_general_case():
    assert tester.two_sum([2, 7, 11, 15], 9) == [1, 2]


def test_negatives():
    assert tester.two_sum([-1, 0], -1) == [1, 2]
