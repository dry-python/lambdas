# -*- coding: utf-8 -*-

from lambdas import _


def test_sub():
    """Ensures that add works correctly."""
    assert (_ - 10)(1) + 1 == -8


def test_rsub():
    """Ensures that add works correctly."""
    assert (10 - _)(1) + (_ - 10)(1) == 0
