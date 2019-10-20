# -*- coding: utf-8 -*-

from lambdas import _


def test_getitem():
    """Ensures that getitem works correctly."""
    assert _['a']({'a': 1}) == 1
