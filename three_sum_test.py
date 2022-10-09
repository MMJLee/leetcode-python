# https://leetcode.com/problems/3sum/

from three_sum import ThreeSum

tester = ThreeSum()


def test_general_case():
    assert tester.three_sum(
        [-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]


def test_no_answer():
    assert tester.three_sum([0, 1, 1]) == []


def test_one_answer():
    assert tester.three_sum([0, 0, 0, 0]) == [[0, 0, 0]]
