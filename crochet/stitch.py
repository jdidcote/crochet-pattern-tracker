from dataclasses import dataclass

from region import Region


@dataclass
class Stitch:
    """
    Class to represent a crochet stitch.
    """
    id: int
    term: str
    symbol: str
    region: Region
