# -*- coding: utf-8 -*-

from lambdas import _MathExpression


def test_complex_expression():
    """Ensures that add works correctly."""
    complex_expression = _MathExpression() * 2 + 1
    assert complex_expression(1) == 3
