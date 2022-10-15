# https://leetcode.com/problems/group-anagrams/

from car_fleet import CarFleet

tester = CarFleet()


def test_general_case_one():
    assert tester.car_fleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3


def test_general_case_two():
    assert tester.car_fleet(100, [0, 2, 4], [4, 2, 1]) == 1


def test_single_case():
    assert tester.car_fleet(10, [3], [3]) == 1
