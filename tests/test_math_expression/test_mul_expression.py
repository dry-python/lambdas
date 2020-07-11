# -*- coding: utf-8 -*-

from lambdas import _MathExpression


def test_mul():
    """Ensures that add works correctly."""
    mul = _MathExpression() * 10
    assert mul(10) == 100


def test_rmul():
    """Ensures that add works correctly."""
    mul = _MathExpression() * 2
    rmul = 2 * _MathExpression()
    assert mul(4) == rmul(4)
