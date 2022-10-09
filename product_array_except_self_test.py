# https://leetcode.com/problems/product-of-array-except-self/
from product_array_except_self import ProductArrayExceptSelf

tester = ProductArrayExceptSelf()


def test_general_case():
    assert tester.product_array_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]


def test_zero_case_one():
    assert tester.product_array_except_self(
        [-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]


def test_zero_case_two():
    assert tester.product_array_except_self([1, 2, 3, 4, 0, 0, 6]) == [
        0, 0, 0, 0, 0, 0, 0]
