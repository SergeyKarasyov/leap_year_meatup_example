from is_leap import is_leap
from test_data import test_data
import pytest

"""
if (year is not divisible by 4) then (it is a common year)
else if (year is not divisible by 100) then (it is a leap year)
else if (year is not divisible by 400) then (it is a common year)
else (it is a leap year)
"""


# dummy tests, may be removed later
def test_is_leap_2000():
    assert True is is_leap(2000)


def test_is_leap_2001():
    assert False is is_leap(2001)


# test according to algo
def test_is_leap_not_div_by_4():
    assert False is is_leap(2015)


def test_is_leap_div_by_4_and_not_div_by_100():
    assert True is is_leap(2016)


def test_is_leap_div_by_4_and_div_by_100_and_not_div_by_400():
    assert False is is_leap(1900)


def test_is_leap_div_by_4_and_div_by_100_and_div_by_400():
    assert True is is_leap(400)


# test with 0
# TODO: is year 0 a valid value?
def test_is_leap_0():
    assert True is is_leap(0)


# test with negative value
# TODO: is year with minus a valid value?
def test_is_leap_minus_2000():
    assert True is is_leap(-2000)


# test with generated data
@pytest.mark.parametrize("year, result", test_data)
def test_is_leap_minus_from_2000_till_2000(year, result):
    print("{} {} {}".format(result, year, is_leap(year)))
    assert result is is_leap(year)
