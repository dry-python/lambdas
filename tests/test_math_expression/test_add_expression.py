# -*- coding: utf-8 -*-

from lambdas import _MathExpression


def test_add():
    """Ensures that add works correctly."""
    add = _MathExpression() + 2
    assert add(1) + 1 == 4


def test_radd():
    """Ensures that add works correctly."""
    add = _MathExpression() + 2
    radd = 2 + _MathExpression()
    assert add(1) == radd(1)
