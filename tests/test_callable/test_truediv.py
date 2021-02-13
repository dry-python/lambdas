# -*- coding: utf-8 -*-

import math

from lambdas import _


def test_truediv():
    """Ensures that add works correctly."""
    math_expression = (_ / 6)
    assert math.isclose(math_expression(39), 6.5)  # type: ignore


def test_rtruediv():
    """Ensures that add works correctly."""
    assert (42 / _)(8) == (_ / 8)(42)
