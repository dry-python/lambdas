# -*- coding: utf-8 -*-

from lambdas import _


def test_truediv():
    """Ensures that add works correctly."""
    assert (_ / 6)(39) == 6.5


def test_rtruediv():
    """Ensures that add works correctly."""
    assert (42 / _)(8) == (_ / 8)(42)
