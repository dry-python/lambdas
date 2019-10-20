# -*- coding: utf-8 -*-

import operator
from typing import Callable, Mapping, TypeVar

T1 = TypeVar('T1')
T2 = TypeVar('T2')


def _fmap(callback):
    def decorator(self, second):
        return lambda first: callback(first, second)
    return decorator


def _unary_fmap(callback):
    def decorator(self):
        return callback
    return decorator


def _flip(callback):
    return lambda first, second: callback(second, first)


class _Callable(object):
    def __getitem__(
        self, key: T1,
    ) -> Callable[[Mapping[T1, T2]], T2]:
        return operator.itemgetter(key)

    __add__: Callable[['_Callable', T1], Callable[[T1], T1]] = _fmap(
        operator.add,
    )
    __mul__: Callable[['_Callable', T1], Callable[[T1], T1]] = _fmap(
        operator.mul,
    )
    __sub__: Callable[['_Callable', T1], Callable[[T1], T1]] = _fmap(
        operator.sub,
    )
    __mod__: Callable[['_Callable', T1], Callable[[T1], T1]] = _fmap(
        operator.mod,
    )
    __pow__: Callable[['_Callable', T1], Callable[[T1], T1]] = _fmap(
        operator.pow,
    )

    __and__: Callable[['_Callable', T1], Callable[[T1], T1]] = _fmap(
        operator.and_,
    )
    __or__: Callable[['_Callable', T1], Callable[[T1], T1]] = _fmap(
        operator.or_,
    )
    __xor__: Callable[['_Callable', T1], Callable[[T1], T1]] = _fmap(
        operator.xor,
    )

    __div__: Callable[['_Callable', T1], Callable[[T1], T1]] = _fmap(
        operator.truediv,
    )
    __divmod__: Callable[['_Callable', T1], Callable[[T1], T1]] = _fmap(divmod)
    __floordiv__: Callable[['_Callable', T1], Callable[[T1], T1]] = _fmap(
        operator.floordiv,
    )
    __truediv__: Callable[['_Callable', T1], Callable[[T1], T1]] = _fmap(
        operator.truediv,
    )

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

    __radd__: Callable[['_Callable', T1], Callable[[T1], T1]] = _fmap(
        _flip(operator.add),
    )
    __rmul__: Callable[['_Callable', T1], Callable[[T1], T1]] = _fmap(
        _flip(operator.mul),
    )
    __rsub__: Callable[['_Callable', T1], Callable[[T1], T1]] = _fmap(
        _flip(operator.sub),
    )
    __rmod__: Callable[['_Callable', T1], Callable[[T1], T1]] = _fmap(
        _flip(operator.mod),
    )
    __rpow__: Callable[['_Callable', T1], Callable[[T1], T1]] = _fmap(
        _flip(operator.pow),
    )
    __rdiv__: Callable[['_Callable', T1], Callable[[T1], T1]] = _fmap(
        _flip(operator.truediv),
    )
    __rdivmod__: Callable[['_Callable', T1], Callable[[T1], T1]] = _fmap(
        _flip(divmod),
    )
    __rtruediv__: Callable[['_Callable', T1], Callable[[T1], T1]] = _fmap(
        _flip(operator.truediv),
    )
    __rfloordiv__: Callable[['_Callable', T1], Callable[[T1], T1]] = _fmap(
        _flip(operator.floordiv),
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


_ = _Callable()  # noqa: WPS122
