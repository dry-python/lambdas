# -*- coding: utf-8 -*-

from lambdas import _


def test_complex_expression():
    """Ensures that add works correctly."""
    assert ((10 ** 5) / (_ % 3) * 9)(5) == 450000.0
