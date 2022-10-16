# https://leetcode.com/problems/permutations/
from typing import List

from permutations import Permutations

tester = Permutations()


def test_general_case_one():
    assert tester.permutations([1, 2, 3]).sort() == [[1, 2, 3], [1, 3, 2], [
        2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]].sort()


def test_general_case_two():
    assert tester.permutations([1, 2, 3, 4]).sort() == [1234, 1243, 1324, 1342, 1423, 1432, 2134, 2143,
                                                        2314, 2341, 2413, 2431, 3124, 3142, 3214, 3241, 3412, 3421, 4123, 4132, 4213, 4231, 4321, 4312].sort()


def test_single_case():
    assert tester.permutations([1]) == [[1]]
