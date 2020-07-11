# -*- coding: utf-8 -*-

from lambdas import _


def test_mul():
    """Ensures that add works correctly."""
    assert (_ * 20)(10) == 200


def test_rmul():
    """Ensures that add works correctly."""
    assert (99 * _)(4) == (_ * 99)(4)
