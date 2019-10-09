#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""module to check if year is the leap one.
if (year is not divisible by 4) then (it is a common year)
else if (year is not divisible by 100) then (it is a leap year)
else if (year is not divisible by 400) then (it is a common year)
else (it is a leap year)
A year that is not a leap year is called a common year.
"""


def is_leap(year: int) -> bool:
    """true if year is leap, false if not. Valid for gregorian calendar"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
