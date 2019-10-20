# -*- coding: utf-8 -*-

from lambdas import _


def test_add():
    """Ensures that add works correctly."""
    assert (_ + 2)(1) == 3


def test_radd():
    """Ensures that add works correctly."""
    assert (2 + _)(1) == (_ + 2)(1)
