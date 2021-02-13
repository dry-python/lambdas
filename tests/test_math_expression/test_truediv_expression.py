# -*- coding: utf-8 -*-

import math

from lambdas import _MathExpression


def test_truediv():
    """Ensures that add works correctly."""
    truediv = _MathExpression() / 2
    assert math.isclose(truediv(9), 4.5)  # type: ignore


def test_rtruediv():
    """Ensures that add works correctly."""
    truediv = _MathExpression() / 2
    rtruediv = 9 / _MathExpression()
    assert truediv(9) == rtruediv(2)
