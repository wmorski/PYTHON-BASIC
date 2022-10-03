"""
Write tests for a read_numbers function.
It should check successful and failed cases
for example:
Test if user inputs: 1, 2, 3, 4
Test if user inputs: 1, 2, Text

Tip: for passing custom values to the input() function
Use unittest.mock patch function
https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch

TIP: for testing builtin input() function create another function which return input() and mock returned value
"""
from unittest.mock import patch

from practice.python_part_2.task_input_output import read_numbers


def test_read_numbers_only_text_input():
    mock_args = ['Text', 'Text']
    with patch('builtins.input') as mocked_input:
        mocked_input.side_effect = mock_args
        result = read_numbers(2)
    assert result == 'No numbers entered'


def test_read_numbers_without_text_input():
    mock_args = ['1', '2', '3', '4']
    with patch('builtins.input') as mocked_input:
        mocked_input.side_effect = mock_args
        result = read_numbers(4)
    assert result == 'Avg: 2.50'


def test_read_numbers_with_text_input():
    mock_args = ['1', '2', 'Text']
    with patch('builtins.input') as mocked_input:
        mocked_input.side_effects = mock_args
        result = read_numbers(3)
    assert result == "Avg: 1.00"
