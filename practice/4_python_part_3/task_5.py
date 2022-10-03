"""
Write a function that makes a request to some url
using urllib. Return status code and decoded response data in utf-8
Examples:
     >>> make_request('http://www.google.com')
     200, 'response data'
"""
from typing import Tuple
from urllib.request import urlopen
from unittest.mock import Mock


def make_request(url: str) -> Tuple[int, str]:
    with urlopen(url) as response:
        return response.status, response.read().decode('utf-8')


"""
Write test for make_request function
Use Mock for mocking request with urlopen https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
Example:
    >>> m = Mock()
    >>> m.method.return_value = 200
    >>> m.method2.return_value = b'some text'
    >>> m.method()
    200
    >>> m.method2()
    b'some text'
"""


def test_make_request():  # run in iterm using pytest task_5.py
    status, data = make_request('https://api.myip.com/')

    m = Mock()
    m.status_code.return_value = 200
    m.response_data.return_value = '{"ip":"193.109.103.128","country":"United Kingdom","cc":"GB"}'

    assert m.status_code() == status
    assert m.response_data() == data

