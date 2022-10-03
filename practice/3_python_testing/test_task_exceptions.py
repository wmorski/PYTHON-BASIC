"""
Write tests for division() function in python_part_2/task_exceptions.py
In case (1,1) it should check if exception were raised
In case (1,0) it should check if return value is None and "Division by 0" printed
If other cases it should check if division is correct

TIP: to test output of print() function use capfd fixture
https://stackoverflow.com/a/20507769
"""
import pytest

from practice.python_part_2.task_exceptions import division, DivisionByOneException


def test_division_ok(capfd):
    assert division(2, 2) == 1
    out, err = capfd.readouterr()
    assert out == "Division finished\n"


def test_division_by_zero(capfd):
    assert division(1, 0) is None
    out, err = capfd.readouterr()
    assert out == "Division by 0\nDivision finished\n"


def test_division_by_one(capfd):
    with pytest.raises(DivisionByOneException):
        division(1, 1)
    out, err = capfd.readouterr()
    assert out == "Division finished\n"
