# -*- coding: utf-8 -*-

from lambdas import _


def test_mod():
    """Ensures that add works correctly."""
    assert (_ % 35)(140) == 0


def test_rmod():
    """Ensures that add works correctly."""
    assert (149 % _)(36) == (_ % 36)(149)
