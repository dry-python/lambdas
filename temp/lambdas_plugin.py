# -*- coding: utf-8 -*-

import types
from typing import Type, Optional, Callable, TypeVar
from typing_extensions import Protocol

from mypy.mro import calculate_mro
from mypy.types import CallableType, Instance, NoneType
from mypy.nodes import NameExpr, ClassDef, Block, AssignmentStmt, TempNode, SymbolTable, TypeInfo
from mypy.plugin import MethodSigContext, Plugin

T = TypeVar('T')


def unusused():
    class Center(Protocol):
        center: int

    runtime_protocol = types.new_class(
        str(ctx.type) + '.' + ctx.context.name + 'Protocol',
        (Protocol, ),
        {ctx.context.name: None},
    )

    runtime_protocol.__annotations__ = {ctx.context.name: int}
    print(runtime_protocol)


def _analyze_lambda(ctx):
    print(ctx)
    print(ctx.context, ctx.context.name)
    print()


    name = str(ctx.type) + '.' + ctx.context.name + 'Protocol'
    class_def = ClassDef(
        name=name,
        defs=Block([
            AssignmentStmt(
                [NameExpr(ctx.context.name)],
                TempNode(NoneType(), no_rhs=True),
            ),
        ]),
        base_type_exprs=[NameExpr('type_extensions.Protocol')],
    )

    type_info = TypeInfo(ctx.api.globals, class_def, name)
    type_info._fullname = name
    calculate_mro(type_info)
    print(type_info.mro)
    type_info.is_protocol = True

    class_def.info = type_info

    return ctx.default_attr_type.copy_modified(
        arg_types=[Instance(type_info, [])],
        variables=[],
    )


class _TypedShortLambdasPlugin(Plugin):
    def get_attribute_hook(
        self,
        fullname: str,
    ):
        if fullname.startswith('lambdas.'):
           print(fullname)
           return _analyze_lambda
        return None


def plugin(version: str) -> Type[Plugin]:
    """Plugin's public API and entrypoint."""
    return _TypedShortLambdasPlugin
