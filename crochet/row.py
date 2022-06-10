from dataclasses import dataclass
from typing import List

from stitch import Stitch


@dataclass
class RowElement:
    """
    A class to represent a stitch and quantity
    """
    stitch: Stitch
    n_stitches: int
    color_change: bool

    def __post_init__(self):
        if self.n_stitches < 0:
            raise ValueError("Number of stitches must be positive")


@dataclass
class Row:
    row_elements: List[RowElement] = None
    row_complete: bool = False

    def __post_init__(self):
        if self.row_elements is None:
            self.row_elements = []


if __name__ == '__main__':
    import random

    from database import StitchDatabase
    from region import Region

    row_seqs = []
    for i in range(5):
        stitch = StitchDatabase().load_stitch(id=i, region=Region('UK'))
        row_seqs.append(
            RowElement(stitch, random.randrange(6), False)
        )

    new_row = Row()
    new_row.add_element(row_seqs[0])