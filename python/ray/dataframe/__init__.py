from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pandas as pd
from pandas import (eval, unique, value_counts, Panel, date_range, MultiIndex)
import threading

pd_version = pd.__version__
pd_major = int(pd_version.split(".")[0])
pd_minor = int(pd_version.split(".")[1])

if pd_major == 0 and pd_minor < 22:
    raise Exception("In order to use Pandas on Ray, please upgrade your Pandas"
                    " version to >= 0.22.")

DEFAULT_NPARTITIONS = 8


def set_npartition_default(n):
    global DEFAULT_NPARTITIONS
    DEFAULT_NPARTITIONS = n


def get_npartitions():
    return DEFAULT_NPARTITIONS


# We import these file after above two function
# because they depend on npartitions.
from .dataframe import DataFrame  # noqa: 402
from .series import Series  # noqa: 402
from .io import (read_csv, read_parquet, read_json, read_html,  # noqa: 402
                 read_clipboard, read_excel, read_hdf, read_feather,  # noqa: 402
                 read_msgpack, read_stata, read_sas, read_pickle,  # noqa: 402
                 read_sql)  # noqa: 402
from .concat import concat  # noqa: 402
from .datetimes import to_datetime  # noqa: 402
from .reshape import get_dummies  # noqa: 402

__all__ = [
    "DataFrame", "Series", "read_csv", "read_parquet", "concat", "eval",
    "unique", "value_counts", "to_datetime", "get_dummies", "Panel",
    "date_range", "MultiIndex"
]

try:
    if threading.current_thread().name == "MainThread":
        import ray
        ray.init()
except AssertionError:
    pass
