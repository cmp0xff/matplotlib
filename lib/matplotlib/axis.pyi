from collections.abc import Callable, Iterable, Sequence
import datetime
from typing import Any, Literal, overload
from typing_extensions import Self  # < Py 3.11

import numpy as np
from numpy.typing import ArrayLike

import matplotlib.artist as martist
from matplotlib import cbook
from matplotlib.axes import Axes
from matplotlib.backend_bases import RendererBase
from matplotlib.lines import Line2D
from matplotlib.text import Text
from matplotlib.ticker import Locator, Formatter
from matplotlib.transforms import Transform, Bbox
from matplotlib.typing import ColorType
from matplotlib.units import ConversionInterface


GRIDLINE_INTERPOLATION_STEPS: int

class Tick(martist.Artist):
    axes: Axes
    tick1line: Line2D
    tick2line: Line2D
    gridline: Line2D
    label1: Text
    label2: Text
    def __init__(
        self,
        axes: Axes,
        loc: float,
        *,
        size: float | None = ...,
        width: float | None = ...,
        color: ColorType | None = ...,
        tickdir: Literal["in", "inout", "out"] | None = ...,
        pad: float | None = ...,
        labelsize: float | None = ...,
        labelcolor: ColorType | None = ...,
        labelfontfamily: str | Sequence[str] | None = ...,
        zorder: float | None = ...,
        gridOn: bool | None = ...,
        tick1On: bool = ...,
        tick2On: bool = ...,
        label1On: bool = ...,
        label2On: bool = ...,
        major: bool = ...,
        labelrotation: float = ...,
        labelrotation_mode: Literal["default", "anchor", "xtick", "ytick"] | None = ...,
        grid_color: ColorType | None = ...,
        grid_linestyle: str | None = ...,
        grid_linewidth: float | None = ...,
        grid_alpha: float | None = ...,
        **kwargs
    ) -> None: ...
    def get_tickdir(self) -> Literal["in", "inout", "out"]: ...
    def get_tick_padding(self) -> float: ...
    def get_children(self) -> list[martist.Artist]: ...
    stale: bool
    def set_pad(self, val: float) -> None: ...
    def get_pad(self) -> None: ...
    def get_loc(self) -> float: ...
    def set_url(self, url: str | None) -> None: ...
    def get_view_interval(self) -> ArrayLike: ...
    def update_position(self, loc: float) -> None: ...

class XTick(Tick):
    __name__: str
    def __init__(self, *args, **kwargs) -> None: ...
    stale: bool
    def update_position(self, loc: float) -> None: ...
    def get_view_interval(self) -> np.ndarray: ...

class YTick(Tick):
    __name__: str
    def __init__(self, *args, **kwargs) -> None: ...
    stale: bool
    def update_position(self, loc: float) -> None: ...
    def get_view_interval(self) -> np.ndarray: ...

class Ticker:
    def __init__(self) -> None: ...
    @property
    def locator(self) -> Locator | None: ...
    @locator.setter
    def locator(self, locator: Locator) -> None: ...
    @property
    def formatter(self) -> Formatter | None: ...
    @formatter.setter
    def formatter(self, formatter: Formatter) -> None: ...

class _LazyTickList:
    def __init__(self, major: bool) -> None: ...
    @overload
    def __get__(self, instance: None, owner: None) -> Self: ...
    @overload
    def __get__(self, instance: Axis, owner: type[Axis]) -> list[Tick]: ...

class Axis(martist.Artist):
    OFFSETTEXTPAD: int
    isDefault_label: bool
    axes: Axes
    major: Ticker
    minor: Ticker
    callbacks: cbook.CallbackRegistry
    label: Text
    offsetText: Text
    labelpad: float
    pickradius: float
    def __init__(self, axes, *, pickradius: float = ...,
                 clear: bool = ...) -> None: ...
    @property
    def isDefault_majloc(self) -> bool: ...
    @isDefault_majloc.setter
    def isDefault_majloc(self, value: bool) -> None: ...
    @property
    def isDefault_majfmt(self) -> bool: ...
    @isDefault_majfmt.setter
    def isDefault_majfmt(self, value: bool) -> None: ...
    @property
    def isDefault_minloc(self) -> bool: ...
    @isDefault_minloc.setter
    def isDefault_minloc(self, value: bool) -> None: ...
    @property
    def isDefault_minfmt(self) -> bool: ...
    @isDefault_minfmt.setter
    def isDefault_minfmt(self, value: bool) -> None: ...
    majorTicks: _LazyTickList
    minorTicks: _LazyTickList
    def get_remove_overlapping_locs(self) -> bool: ...
    def set_remove_overlapping_locs(self, val: bool) -> None: ...
    @property
    def remove_overlapping_locs(self) -> bool: ...
    @remove_overlapping_locs.setter
    def remove_overlapping_locs(self, val: bool) -> None: ...
    stale: bool
    def set_label_coords(
        self, x: float, y: float, transform: Transform | None = ...
    ) -> None: ...
    def get_transform(self) -> Transform: ...
    def get_scale(self) -> str: ...
    def limit_range_for_scale(
        self, vmin: float, vmax: float
    ) -> tuple[float, float]: ...
    def get_children(self) -> list[martist.Artist]: ...
    # TODO units
    converter: Any
    units: Any
    def clear(self) -> None: ...
    def reset_ticks(self) -> None: ...
    def minorticks_on(self) -> None: ...
    def minorticks_off(self) -> None: ...
    def set_tick_params(
        self,
        which: Literal["major", "minor", "both"] = ...,
        reset: bool = ...,
        **kwargs
    ) -> None: ...
    def get_tick_params(
        self, which: Literal["major", "minor"] = ...
    ) -> dict[str, Any]: ...
    def get_view_interval(self) -> tuple[float, float]: ...
    def set_view_interval(
        self, vmin: float, vmax: float, ignore: bool = ...
    ) -> None: ...
    def get_data_interval(self) -> tuple[float, float]: ...
    def set_data_interval(
        self, vmin: float, vmax: float, ignore: bool = ...
    ) -> None: ...
    def get_inverted(self) -> bool: ...
    def set_inverted(self, inverted: bool) -> None: ...
    def set_default_intervals(self) -> None: ...
    def get_tightbbox(
        self, renderer: RendererBase | None = ..., *, for_layout_only: bool = ...
    ) -> Bbox | None: ...
    def get_tick_padding(self) -> float: ...
    def get_gridlines(self) -> list[Line2D]: ...
    def get_label(self) -> Text: ...
    def get_offset_text(self) -> Text: ...
    def get_pickradius(self) -> float: ...
    def get_majorticklabels(self) -> list[Text]: ...
    def get_minorticklabels(self) -> list[Text]: ...
    def get_ticklabels(
        self, minor: bool = ..., which: Literal["major", "minor", "both"] | None = ...
    ) -> list[Text]: ...
    def get_majorticklines(self) -> list[Line2D]: ...
    def get_minorticklines(self) -> list[Line2D]: ...
    def get_ticklines(self, minor: bool = ...) -> list[Line2D]: ...
    def get_majorticklocs(self) -> np.ndarray: ...
    def get_minorticklocs(self) -> np.ndarray: ...
    def get_ticklocs(self, *, minor: bool = ...) -> np.ndarray: ...
    def get_ticks_direction(self, minor: bool = ...) -> np.ndarray: ...
    def get_label_text(self) -> str: ...
    def get_major_locator(self) -> Locator: ...
    def get_minor_locator(self) -> Locator: ...
    def get_major_formatter(self) -> Formatter: ...
    def get_minor_formatter(self) -> Formatter: ...
    def get_major_ticks(self, numticks: int | None = ...) -> list[Tick]: ...
    def get_minor_ticks(self, numticks: int | None = ...) -> list[Tick]: ...
    def grid(
        self,
        visible: bool | None = ...,
        which: Literal["major", "minor", "both"] = ...,
        **kwargs
    ) -> None: ...
    # TODO units
    def update_units(self, data): ...
    def have_units(self) -> bool: ...
    def convert_units(self, x): ...
    def get_converter(self) -> ConversionInterface | None: ...
    def set_converter(self, converter: ConversionInterface) -> None: ...
    def set_units(self, u) -> None: ...
    def get_units(self): ...
    def set_label_text(
        self, label: str, fontdict: dict[str, Any] | None = ..., **kwargs
    ) -> Text: ...
    def set_major_formatter(
        self, formatter: Formatter | str | Callable[[float, float], str]
    ) -> None: ...
    def set_minor_formatter(
        self, formatter: Formatter | str | Callable[[float, float], str]
    ) -> None: ...
    def set_major_locator(self, locator: Locator) -> None: ...
    def set_minor_locator(self, locator: Locator) -> None: ...
    def set_pickradius(self, pickradius: float) -> None: ...
    def set_ticklabels(
        self,
        labels: Iterable[str | Text],
        *,
        minor: bool = ...,
        fontdict: dict[str, Any] | None = ...,
        **kwargs
    ) -> list[Text]: ...
    def set_ticks(
        self,
        ticks: ArrayLike,
        labels: Iterable[str] | None = ...,
        *,
        minor: bool = ...,
        **kwargs
    ) -> list[Tick]: ...
    def axis_date(self, tz: str | datetime.tzinfo | None = ...) -> None: ...
    def get_tick_space(self) -> int: ...
    def get_label_position(self) -> Literal["top", "bottom"]: ...
    def set_label_position(
        self, position: Literal["top", "bottom", "left", "right"]
    ) -> None: ...
    def get_minpos(self) -> float: ...

class XAxis(Axis):
    __name__: str
    axis_name: str
    def __init__(self, *args, **kwargs) -> None: ...
    label_position: Literal["bottom", "top"]
    stale: bool
    def set_label_position(self, position: Literal["bottom", "top"]) -> None: ...  # type: ignore[override]
    def set_ticks_position(
        self, position: Literal["top", "bottom", "both", "default", "none"]
    ) -> None: ...
    def tick_top(self) -> None: ...
    def tick_bottom(self) -> None: ...
    def get_ticks_position(self) -> Literal["top", "bottom", "default", "unknown"]: ...
    def get_tick_space(self) -> int: ...

class YAxis(Axis):
    __name__: str
    axis_name: str
    def __init__(self, *args, **kwargs) -> None: ...
    label_position: Literal["left", "right"]
    stale: bool
    def set_label_position(self, position: Literal["left", "right"]) -> None: ...  # type: ignore[override]
    def set_offset_position(self, position: Literal["left", "right"]) -> None: ...
    def set_ticks_position(
        self, position: Literal["left", "right", "both", "default", "none"]
    ) -> None: ...
    def tick_right(self) -> None: ...
    def tick_left(self) -> None: ...
    def get_ticks_position(self) -> Literal["left", "right", "default", "unknown"]: ...
    def get_tick_space(self) -> int: ...
