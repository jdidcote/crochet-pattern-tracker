from dataclasses import dataclass
from typing import List

from row import Row

@dataclass
class Pattern:
    """
    Class to represent a pattern.

    A pattern is a collection of rows.
    """
    rows: List[Row]
