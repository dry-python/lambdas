# -*- coding: utf-8 -*-

from lambdas import _


def test_pow():
    """Ensures that add works correctly."""
    assert (_ ** 3)(2) == 8


def test_rpow():
    """Ensures that add works correctly."""
    assert (3 ** _)(4) == (_ ** 4)(3)
