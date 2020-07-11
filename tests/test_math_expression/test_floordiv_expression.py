# -*- coding: utf-8 -*-

from lambdas import _MathExpression


def test_floordiv():
    """Ensures that add works correctly."""
    floordiv = _MathExpression() // 2
    assert floordiv(5) == 2


def test_rfloordiv():
    """Ensures that add works correctly."""
    floordiv = _MathExpression() // 2
    rfloordiv = 5 // _MathExpression()
    assert floordiv(5) == rfloordiv(2)
