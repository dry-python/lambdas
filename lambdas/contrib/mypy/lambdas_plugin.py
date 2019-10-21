# -*- coding: utf-8 -*-

from typing import Type

from mypy.nodes import MemberExpr
from mypy.plugin import AttributeContext, Plugin


def _mutate_field_name(ctx):
    default = ctx.default_attr_type.arg_types[0]
    if not default.type.names:
        return

    old_field_name = next(iter(default.type.names.keys()))
    actual_field = default.type.names[old_field_name].copy()
    actual_field.cross_ref = None

    actual_field.node._name = ctx.context.name
    fullname = actual_field.node._fullname.rsplit('.', 1)
    fullname[-1] = ctx.context.name
    actual_field.node._fullname = '.'.join(fullname)

    default.type.names[ctx.context.name] = actual_field
    default.type.names.pop(old_field_name)


def _analyze_lambda(plugin: Plugin):
    def factory(ctx: AttributeContext):
        if isinstance(ctx.context, MemberExpr):
            _mutate_field_name(ctx)

        return ctx.default_attr_type
    return factory


class _TypedShortLambdasPlugin(Plugin):
    def get_attribute_hook(self, fullname: str):
        """
        This method is called on expressions like: ``_.attr``.

        We use it to change the default generic protocol field name.
        In case it was called as ``_.attr`` we change the name to ``attr``.

        See also:
            https://github.com/python/mypy/blob/master/mypy/nodes.py
            https://github.com/python/mypy/blob/master/mypy/types.py
            https://github.com/python/mypy/blob/master/mypy/plugin.py

        """
        if fullname.startswith('lambdas._Callable.'):
            return _analyze_lambda(self)
        return None


def plugin(version: str) -> Type[Plugin]:
    """Plugin's public API and entrypoint."""
    return _TypedShortLambdasPlugin
