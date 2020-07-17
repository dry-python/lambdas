# -*- coding: utf-8 -*-

from lambdas import _


def test_floordiv():
    """Ensures that add works correctly."""
    assert (_ // 5)(33) == 6


def test_rfloordiv():
    """Ensures that add works correctly."""
    assert (_ // 5)(33) == (33 // _)(5)
