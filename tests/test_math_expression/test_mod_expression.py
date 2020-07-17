# -*- coding: utf-8 -*-

from lambdas import _MathExpression


def test_mod():
    """Ensures that add works correctly."""
    mod = _MathExpression() % 3
    assert mod(25) == 1


def test_rmod():
    """Ensures that add works correctly."""
    mod = _MathExpression() % 3
    rmod = 25 % _MathExpression()
    assert mod(25) == rmod(3)
