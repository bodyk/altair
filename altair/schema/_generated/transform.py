# This file auto-generated by `_schema_parser.py`.
# Do not modify this file directly.

import traitlets as T
from ..baseobject import BaseObject
from .vgformula import VgFormula


class Transform(BaseObject):
    calculate = T.List(T.Instance(VgFormula, allow_none=True, default_value=None), allow_none=True, default_value=None, help="""Calculate new field(s) using the provided expresssion(s).""")
    filter = T.Unicode(allow_none=True, default_value=None, help="""A string containing the filter Vega expression.""")
    filterNull = T.Bool(allow_none=True, default_value=None, help="""Filter null values from the data.""")

