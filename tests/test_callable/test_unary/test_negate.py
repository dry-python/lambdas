# -*- coding: utf-8 -*-

from lambdas import _


def test_negate():
    """Ensures that negate works correctly."""
    assert (-_)(1) - 1 == -2
