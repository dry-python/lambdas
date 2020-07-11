# -*- coding: utf-8 -*-

from lambdas import _MathExpression


def test_sub():
    """Ensures that add works correctly."""
    sub = _MathExpression() - 4
    assert sub(4) == 0


def test_rsub():
    """Ensures that add works correctly."""
    sub = _MathExpression() - 4
    rsub = 4 - _MathExpression()
    assert rsub(1) + sub(1) == 0
