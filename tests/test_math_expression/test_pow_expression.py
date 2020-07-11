# -*- coding: utf-8 -*-

from lambdas import _MathExpression


def test_pow():
    """Ensures that add works correctly."""
    pow_ = _MathExpression() ** 2
    assert pow_(3) == 9


def test_rpow():
    """Ensures that add works correctly."""
    pow_ = _MathExpression() ** 2
    rpow = 3 ** _MathExpression()
    assert pow_(3) == rpow(2)
