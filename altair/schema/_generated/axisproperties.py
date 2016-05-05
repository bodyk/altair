# This file auto-generated by `_schema_parser.py`.
# Do not modify this file directly.

import traitlets as T
from ..baseobject import BaseObject
from .axisorient import AxisOrient


class AxisProperties(BaseObject):
    axisWidth = T.CFloat(allow_none=True, default_value=None, help="""Width of the axis line.""")
    characterWidth = T.CFloat(allow_none=True, default_value=None, help="""Character width for automatically determining title max length.""")
    format = T.Unicode(allow_none=True, default_value=None, help="""The formatting pattern for axis labels.""")
    grid = T.Bool(allow_none=True, default_value=None, help="""A flag indicate if gridlines should be created in addition to ticks.""")
    labelAlign = T.Unicode(allow_none=True, default_value=None, help="""Text alignment for the Label.""")
    labelAngle = T.CFloat(allow_none=True, default_value=None, help="""The rotation angle of the axis labels.""")
    labelBaseline = T.Unicode(allow_none=True, default_value=None, help="""Text baseline for the label.""")
    labelMaxLength = T.CFloat(allow_none=True, min=1, default_value=None, help="""Truncate labels that are too long.""")
    labels = T.Bool(allow_none=True, default_value=None, help="""Enable or disable labels.""")
    layer = T.Unicode(allow_none=True, default_value=None, help="""A string indicating if the axis (and any gridlines) should be placed above or below the data marks.""")
    offset = T.CFloat(allow_none=True, default_value=None, help="""The offset, in pixels, by which to displace the axis from the edge of the enclosing group or data rectangle.""")
    orient = AxisOrient(allow_none=True, default_value=None, help="""The orientation of the axis.""")
    properties = T.Any(allow_none=True, default_value=None, help="""Optional mark property definitions for custom axis styling.""")
    shortTimeLabels = T.Bool(allow_none=True, default_value=None, help="""Whether month and day names should be abbreviated.""")
    subdivide = T.CFloat(allow_none=True, default_value=None, help="""If provided, sets the number of minor ticks between major ticks (the value 9 results in decimal subdivision).""")
    tickPadding = T.CFloat(allow_none=True, default_value=None, help="""The padding, in pixels, between ticks and text labels.""")
    tickSize = T.CFloat(allow_none=True, min=0, default_value=None, help="""The size, in pixels, of major, minor and end ticks.""")
    tickSizeEnd = T.CFloat(allow_none=True, min=0, default_value=None, help="""The size, in pixels, of end ticks.""")
    tickSizeMajor = T.CFloat(allow_none=True, min=0, default_value=None, help="""The size, in pixels, of major ticks.""")
    tickSizeMinor = T.CFloat(allow_none=True, min=0, default_value=None, help="""The size, in pixels, of minor ticks.""")
    ticks = T.CFloat(allow_none=True, min=0, default_value=None, help="""A desired number of ticks, for axes visualizing quantitative scales.""")
    title = T.Unicode(allow_none=True, default_value=None, help="""A title for the axis.""")
    titleMaxLength = T.CFloat(allow_none=True, min=0, default_value=None, help="""Max length for axis title if the title is automatically generated from the field's description.""")
    titleOffset = T.CFloat(allow_none=True, default_value=None, help="""A title offset value for the axis.""")
    values = T.List(T.CFloat(allow_none=True, default_value=None), allow_none=True, default_value=None)

