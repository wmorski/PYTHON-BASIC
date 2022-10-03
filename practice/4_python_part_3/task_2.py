"""
Write function which executes custom operation from math module
for given arguments.
Restrition: math function could take 1 or 2 arguments
If given operation does not exists, raise OperationNotFoundException
Examples:
     >>> math_calculate('log', 1024, 2)
     10.0
     >>> math_calculate('ceil', 10.7)
     11
     >>> math_calculate('unknown_function', 10, 10)
     10
     >>> math_calculate('sqrt', 4)
     2.0
"""
import math
import pytest


class OperationNotFoundException(AttributeError):
    pass


def math_calculate(function: str, *args):
    try:
        if len(args) > 2:
            print('Restriction: math function could take 1 or 2 arguments')
            return None

        func = getattr(math, function)

    except AttributeError:
        raise OperationNotFoundException("Given operation does not exist")

    else:
        return func(*args)


"""
Write tests for math_calculate function
"""


@pytest.mark.parametrize('test_input, expected', [
    (['log', 1024, 2, 2], 10)
])
def test_math_calculate_more_args(test_input, expected, capfd):
    assert math_calculate(test_input[0], test_input[1], test_input[2], test_input[3]) is None
    out, err = capfd.readouterr()
    assert out == 'Restriction: math function could take 1 or 2 arguments\n'


@pytest.mark.parametrize('test_input, expected', [(['log', 1024, 2], 10)])
def test_math_calculate_2_args(test_input, expected):
    result = math_calculate(test_input[0], test_input[1], test_input[2])
    assert result == expected


@pytest.mark.parametrize('test_input, expected', [(['ceil', 10.7], 11), (['sqrt', 4], 2)])
def test_math_calculate_1_arg(test_input, expected):
    result = math_calculate(test_input[0], test_input[1])
    assert result == expected


def test_math_calculate_exception():
    with pytest.raises(OperationNotFoundException) as e:
        math_calculate('unknown_function', 10, 10)
    assert "Given operation does not exist" in str(e.value)
