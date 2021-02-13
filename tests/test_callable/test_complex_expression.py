# -*- coding: utf-8 -*-

import math

from lambdas import _


def test_complex_expression():
    """Ensures that add works correctly."""
    complex_expression = ((10 ** 5) / (_ % 3) * 9)
    assert math.isclose(complex_expression(5), 450000.0)  # type: ignore
