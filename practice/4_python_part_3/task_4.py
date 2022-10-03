"""
Create virtual environment and install Faker package only for this venv.
Write command line tool which will receive int as a first argument and one or more named arguments
 and generates defined number of dicts separated by new line.
Exec format:
`$python task_4.py NUMBER --FIELD=PROVIDER [--FIELD=PROVIDER...]`
where:
NUMBER - positive number of generated instances
FIELD - key used in generated dict
PROVIDER - name of Faker provider
Example:
`$python task_4.py 2 --fake-address=address --some_name=name`
{"some_name": "Chad Baird", "fake-address": "62323 Hobbs Green\nMaryshire, WY 48636"}
{"some_name": "Courtney Duncan", "fake-address": "8107 Nicole Orchard Suite 762\nJosephchester, WI 05981"}
"""

import argparse
import re
import sys
import unittest
from unittest import mock
from unittest.mock import Mock

from faker import Faker


def print_name_address(args: argparse.Namespace) -> None:
    args_dict = vars(args)

    fake = Faker()

    for _ in range(args.number):
        fake_dict = {}
        for field, provider in args_dict.items():
            if field == 'number':
                continue
            provider = getattr(fake, provider)
            fake_dict[field] = provider()
        print(fake_dict)


def create_namespace():
    parser = argparse.ArgumentParser(description="generate dicts with fake info")

    parser.add_argument('number', type=int)

    # Add optional arguments to the parser
    for arg in sys.argv[2:]:
        parser.add_argument(arg.split('=')[0])

    return parser.parse_args()


if __name__ == "__main__":
    print_name_address(create_namespace())

"""
Write test for print_name_address function
Use Mock for mocking args argument https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
Example:
    >>> m = Mock()
    >>> m.method.return_value = 123
    >>> m.method()
    123
"""


class TestPrintNameAddress(unittest.TestCase):
    def setUp(self) -> None:
        self.mock = Mock()
        self.mock.two_args = argparse.Namespace(**{'number': 2, 'fake-name': 'name', 'fake-address': 'address'})
        self.mock.one_arg = argparse.Namespace(**{'number': 3, 'fake-name': 'name'})

    @mock.patch('builtins.print')
    def test_print_two_args(self, mock_print):
        print_name_address(self.mock.two_args)

        for call in mock_print.call_args_list:
            check_name = re.search("\'fake-name\':", str(call))
            check_address = re.search("\'fake-address\':", str(call))
            self.assertTrue(check_name and check_address)

        self.assertTrue(len(mock_print.mock_calls) == 2)

    @mock.patch('builtins.print')
    def test_print_one_arg(self, mock_print):
        print_name_address(self.mock.one_arg)

        for call in mock_print.call_args_list:
            check_name = re.search("\'fake-name\':", str(call))
            check_address = re.search("\'fake-address\':", str(call))
            self.assertTrue(check_name and not check_address)

        self.assertTrue(len(mock_print.mock_calls) == 3)


def test_print_name_address(capfd):
    m = Mock()
    m.create_namespace.return_value = argparse.Namespace(number=1, fake_name='name', fake_address='address')
    print_name_address(m.create_namespace())
    out, err = capfd.readouterr()
    assert bool(re.search("\'fake_name\':", out)) is True
    assert re.search("\'fake_address\':", out)
