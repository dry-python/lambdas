# -*- coding: utf-8 -*-

import operator
from functools import partial, reduce
from typing import Callable, List, Mapping, TypeVar, Union

from typing_extensions import Protocol

T1 = TypeVar('T1')
T2 = TypeVar('T2')

_Number = Union[int, float, complex]


def _fmap(callback):  # pragma: nocover
    # TODO: Remove `pragma` after https://github.com/dry-python/lambdas/issues/4
    """Convers callback to instance method with two arguments."""
    def decorator(self, second):
        return lambda first: callback(first, second)
    return decorator


def _unary_fmap(callback):
    """Convers callback to unary instance method."""
    def decorator(self):
        return callback
    return decorator


def _flip(callback):
    """Flips arguments: the first one becomes the second."""
    return lambda first, second: callback(second, first)


class _LambdaDynamicProtocol(Protocol[T1]):
    """
    This is one of the most complicated parts in this library.

    This is a generic protocol definition that works fine,
    except it cannot change the field name in runtime.

    And we need this field name to change when we call ``_.some``.
    When this happens we use our ``mypy`` plugin
    to change the field name from ``lambdas_generic_field`` to ``some``.

    And it continues to work as is.
    """

    lambdas_generic_field: T1


class _MathExpression(object):  # noqa: WPS214
    """
    Mathmatical expression callable class.

    This class helps us to build an callable with complex mathematical
    expression, basically it's the substitute of `x` in a expression.
    When we call this class the number passed trought the instance will be
    the `x`.

    See the example below:

        >>> from lambdas import _MathExpression
        >>> complex_expression = (10 ** 2) / _MathExpression() * 10
        >>> complex_expression(2)
        500.0

    """

    def __init__(self) -> None:
        self._operations: List[Callable[[_Number], _Number]] = []

    def __call__(self, number: _Number) -> _Number:
        first_operation, *rest_of_the_operations = self._operations
        return reduce(
            lambda partial_result, operation: operation(partial_result),
            rest_of_the_operations,
            first_operation(number),
        )

    def __add__(self, other: _Number) -> '_MathExpression':
        return self._add_operation(_flip(operator.add), other)

    def __sub__(self, other: _Number) -> '_MathExpression':
        return self._add_operation(_flip(operator.sub), other)

    def __mul__(self, other: _Number) -> '_MathExpression':
        return self._add_operation(_flip(operator.mul), other)

    def __floordiv__(self, other: _Number) -> '_MathExpression':
        return self._add_operation(_flip(operator.floordiv), other)

    def __truediv__(self, other: _Number) -> '_MathExpression':
        return self._add_operation(_flip(operator.truediv), other)

    def __mod__(self, other: _Number) -> '_MathExpression':
        return self._add_operation(_flip(operator.mod), other)

    def __pow__(self, other: _Number) -> '_MathExpression':
        return self._add_operation(_flip(operator.pow), other)

    def __radd__(self, other: _Number) -> '_MathExpression':
        return self._add_operation(operator.add, other)

    def __rsub__(self, other: _Number) -> '_MathExpression':
        return self._add_operation(operator.sub, other)

    def __rmul__(self, other: _Number) -> '_MathExpression':
        return self._add_operation(operator.mul, other)

    def __rfloordiv__(self, other: _Number) -> '_MathExpression':
        return self._add_operation(operator.floordiv, other)

    def __rtruediv__(self, other: _Number) -> '_MathExpression':
        return self._add_operation(operator.truediv, other)

    def __rmod__(self, other: _Number) -> '_MathExpression':
        return self._add_operation(operator.mod, other)

    def __rpow__(self, other: _Number) -> '_MathExpression':
        return self._add_operation(operator.pow, other)

    def _add_operation(
        self,
        operation: Callable[[_Number, _Number], _Number],
        other: _Number,
    ) -> '_MathExpression':
        self._operations.append(partial(operation, other))
        return self


class _Callable(object):  # noqa: WPS214
    """
    Short lambda implementation.

    It is useful when you have
    a lot of single-argument ``lambda`` functions here and there.

    It can be used like so:

        >>> from lambdas import _
        >>> response = [{'count': 3}, {'count': 1}, {'count': 2}]
        >>> sorted(response, key=_['count'])
        [{'count': 1}, {'count': 2}, {'count': 3}]

    """

    def __getattr__(
        self,
        key: str,
    ) -> Callable[[_LambdaDynamicProtocol[T1]], T1]:
        return operator.attrgetter(key)

    def __getitem__(
        self, key: T1,
    ) -> Callable[[Mapping[T1, T2]], T2]:
        return operator.itemgetter(key)

    def __add__(self, other: _Number) -> _MathExpression:
        return _MathExpression() + other

    def __sub__(self, other: _Number) -> _MathExpression:
        return _MathExpression() - other

    def __mul__(self, other: _Number) -> _MathExpression:
        return _MathExpression() * other

    def __floordiv__(self, other: _Number) -> _MathExpression:
        return _MathExpression() // other

    def __truediv__(self, other: _Number) -> _MathExpression:
        return _MathExpression() / other

    def __mod__(self, other: _Number) -> _MathExpression:
        return _MathExpression() % other

    def __pow__(self, other: _Number) -> _MathExpression:
        return _MathExpression() ** other

    def __radd__(self, other: _Number) -> _MathExpression:
        return other + _MathExpression()

    def __rsub__(self, other: _Number) -> _MathExpression:
        return other - _MathExpression()

    def __rmul__(self, other: _Number) -> _MathExpression:
        return other * _MathExpression()

    def __rfloordiv__(self, other: _Number) -> _MathExpression:
        return other // _MathExpression()

    def __rtruediv__(self, other: _Number) -> _MathExpression:
        return other / _MathExpression()

    def __rmod__(self, other: _Number) -> _MathExpression:
        return other % _MathExpression()  # noqa: S001

    def __rpow__(self, other: _Number) -> _MathExpression:
        return other ** _MathExpression()

    __and__: Callable[['_Callable', T1], Callable[[T1], T1]] = _fmap(
        operator.and_,
    )
    __or__: Callable[['_Callable', T1], Callable[[T1], T1]] = _fmap(
        operator.or_,
    )
    __xor__: Callable[['_Callable', T1], Callable[[T1], T1]] = _fmap(
        operator.xor,
    )
    __divmod__: Callable[['_Callable', T1], Callable[[T1], T1]] = _fmap(divmod)

    __lshift__: Callable[['_Callable', T1], Callable[[T1], T1]] = _fmap(
        operator.lshift,
    )
    __rshift__: Callable[['_Callable', T1], Callable[[T1], T1]] = _fmap(
        operator.rshift,
    )

    __lt__: Callable[['_Callable', T1], Callable[[T1], T1]] = _fmap(
        operator.lt,
    )
    __le__: Callable[['_Callable', T1], Callable[[T1], T1]] = _fmap(
        operator.le,
    )
    __gt__: Callable[['_Callable', T1], Callable[[T1], T1]] = _fmap(
        operator.gt,
    )
    __ge__: Callable[['_Callable', T1], Callable[[T1], T1]] = _fmap(
        operator.ge,
    )
    __eq__: Callable[
        ['_Callable', object], Callable[[object], bool],
    ] = _fmap(  # type: ignore
        operator.eq,
    )
    __ne__: Callable[
        ['_Callable', object], Callable[[object], bool],
    ] = _fmap(  # type: ignore
        operator.ne,
    )

    __neg__: Callable[['_Callable'], Callable[[T1], T1]] = _unary_fmap(
        operator.neg,
    )
    __pos__: Callable[['_Callable'], Callable[[T1], T1]] = _unary_fmap(
        operator.pos,
    )
    __invert__: Callable[['_Callable'], Callable[[T1], T1]] = _unary_fmap(
        operator.invert,
    )

    __rdivmod__: Callable[['_Callable', T1], Callable[[T1], T1]] = _fmap(
        _flip(divmod),
    )

    __rlshift__: Callable[['_Callable', T1], Callable[[T1], T1]] = _fmap(
        _flip(operator.lshift),
    )
    __rrshift__: Callable[['_Callable', T1], Callable[[T1], T1]] = _fmap(
        _flip(operator.rshift),
    )

    __rand__: Callable[['_Callable', T1], Callable[[T1], T1]] = _fmap(
        _flip(operator.and_),
    )
    __ror__: Callable[['_Callable', T1], Callable[[T1], T1]] = _fmap(
        _flip(operator.or_),
    )
    __rxor__: Callable[['_Callable', T1], Callable[[T1], T1]] = _fmap(
        _flip(operator.xor),
    )


#: Our main alias for the lambda object:
_ = _Callable()  # noqa: WPS122
