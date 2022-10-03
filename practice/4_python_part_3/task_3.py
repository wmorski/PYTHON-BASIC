"""
Write a function which detects if entered string is http/https domain name with optional slash at the and
Restriction: use re module
Note that address may have several domain levels
    >>> is_http_domain('http://wikipedia.org')
    True
    >>> is_http_domain('https://ru.wikipedia.org/')
    True
    >>> is_http_domain('griddynamics.com')
    False
"""
import re

import pytest

# ^(http(s)?:\/\/)([a-zA-Z0-9-]+\.)?[a-zA-Z0-9-]+\.[a-zA-Z]+(\/)?$
# https://regexr.com/6tbd7
# https://www.regextester.com/105539


def is_http_domain(domain: str) -> bool:
    pattern = re.compile("^(http(s)?://)([a-zA-Z0-9-]+.)?[a-zA-Z0-9-]+.[a-zA-Z]+(/)?$")
    return bool(re.match(pattern, domain))


"""
write tests for is_http_domain function
"""


@pytest.mark.parametrize('test_input, expected',
                         [('http://wikipedia.org', True),
                          ('https://ru.wikipedia.org/', True),
                          ('griddynamics.com', False)
                          ])
def test_is_http_domain(test_input, expected):
    assert is_http_domain(test_input) == expected
