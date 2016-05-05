# This file auto-generated by `_schema_parser.py`.
# Do not modify this file directly.

import traitlets as T
from ..baseobject import BaseObject


class ScaleConfig(BaseObject):
    bandSize = T.CFloat(allow_none=True, min=0, default_value=None, help="""Default band size for (1) `y` ordinal scale,

and (2) `x` ordinal scale when the mark is not `text`.""")
    barSizeRange = T.List(T.CFloat(allow_none=True, default_value=None), allow_none=True, default_value=None, help="""Default range for bar size scale.""")
    fontSizeRange = T.List(T.CFloat(allow_none=True, default_value=None), allow_none=True, default_value=None, help="""Default range for font size scale.""")
    includeRawDomain = T.Bool(allow_none=True, default_value=None)
    nominalColorRange = T.Union([T.Unicode(allow_none=True, default_value=None), T.List(T.Unicode(allow_none=True, default_value=None), allow_none=True, default_value=None)])
    padding = T.CFloat(allow_none=True, default_value=None, help="""Default padding for `x` and `y` ordinal scales.""")
    pointSizeRange = T.List(T.CFloat(allow_none=True, default_value=None), allow_none=True, default_value=None, help="""Default range for bar size scale.""")
    round = T.Bool(allow_none=True, default_value=None, help="""If true, rounds numeric output values to integers.""")
    sequentialColorRange = T.Union([T.Unicode(allow_none=True, default_value=None), T.List(T.Unicode(allow_none=True, default_value=None), allow_none=True, default_value=None)])
    shapeRange = T.Union([T.Unicode(allow_none=True, default_value=None), T.List(T.Unicode(allow_none=True, default_value=None), allow_none=True, default_value=None)])
    textBandWidth = T.CFloat(allow_none=True, min=0, default_value=None, help="""Default band width for `x` ordinal scale when is mark is `text`.""")

