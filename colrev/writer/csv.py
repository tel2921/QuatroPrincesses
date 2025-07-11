#! /usr/bin/env python
"""Function to write csv files"""
from __future__ import annotations

import pandas as pd

from colrev.constants import Fields

FIELDS = [
    Fields.ID,
    Fields.ENTRYTYPE,
    Fields.TITLE,
    Fields.AUTHOR,
    Fields.YEAR,
    Fields.JOURNAL,
    Fields.BOOKTITLE,
    Fields.VOLUME,
    Fields.NUMBER,
    Fields.PAGES,
    Fields.DOI,
    Fields.URL,
    Fields.FILE,
]


def to_dataframe(*, records_dict: dict) -> pd.DataFrame:
    """Convert a records dict to a pandas DataFrame"""
    data = []
    additional_fields = [x for x in list(records_dict) if x not in FIELDS]
    for record_id in sorted(records_dict.keys()):
        record_dict = records_dict[record_id]
        row = {}
        for field in FIELDS + additional_fields:
            if field in record_dict:
                row[field] = record_dict[field]
            else:
                row[field] = ""
        data.append(row)
    return pd.DataFrame(data)


def write_file(*, records_dict: dict, filename: str) -> None:
    """Write a csv file from a records dict"""
    data_frame = to_dataframe(records_dict=records_dict)
    data_frame.to_csv(filename, index=False)
