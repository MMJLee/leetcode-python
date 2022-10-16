# https://leetcode.com/problems/subsets/
from typing import List

from subsets import Subsets

tester = Subsets()


def test_general_case():
    assert tester.subsets([1, 2, 3]).sort() == [[], [1], [2], [
        1, 2], [3], [1, 3], [2, 3], [1, 2, 3]].sort()


def test_single_case():
    assert tester.subsets([0]).sort() == [[], [0]].sort()
