# https://leetcode.com/problems/top-k-frequent-elements/

from top_k_elements import TopKElements

tester = TopKElements()


def test_general_case():
    assert tester.top_k_elements([1, 1, 1, 2, 2, 3], 2) == [1, 2]


def test_single_element():
    assert tester.top_k_elements([2], 1) == [2]


def test_one_type_element():
    assert tester.top_k_elements([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1) == [1]
