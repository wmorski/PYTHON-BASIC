"""
using datetime module find number of days from custom date to now
Custom date is a string with format "2021-12-24"
If entered string pattern does not match, raise a custom Exception
If entered date is from future, return negative value for number of days
    >>> calculate_days('2021-10-07')  # for this example today is 6 october 2021
    -1
    >>> calculate_days('2021-10-05')
    1
    >>> calculate_days('10-07-2021')
    WrongFormatException
"""
from datetime import datetime
import pytest


class WrongFormatException(Exception):
    pass


def calculate_days(from_date: str) -> int:
    try:
        from_date = datetime.strptime(from_date, "%Y-%m-%d")
        now = datetime.today()
        return (now - from_date).days
    except ValueError:
        raise WrongFormatException


"""
Write tests for calculate_days function
Note that all tests should pass regardless of the day test was run
Tip: for mocking datetime.now() use https://pypi.org/project/pytest-freezegun/
"""
parameters = [('2022-09-01', 2), ('2022-09-03', 0), ('2022-09-04', -1), ('2022-09-05', -2), ('2022-09-10', -7)]


@pytest.mark.freeze_time('2022-09-03')
@pytest.mark.parametrize('test_input, expected', parameters)
def test_calculate_days(test_input, expected):
    assert calculate_days(test_input) == expected


def test_calculate_days_exception(capfd):
    with pytest.raises(WrongFormatException):
        calculate_days('03-09-2022')
