# -*- coding: utf-8 -*-

from lambdas import _


class _ForTest(object):
    def __init__(self) -> None:
        self.first = 1
        self.second = 'a'


def test_getattr_attr():
    """Ensures that getattr works correctly."""
    assert (_.first)(_ForTest()) + 1 == 2
    assert (_.second)(_ForTest()) == 'a'
