from dataclasses import dataclass

from stitch import Stitch


@dataclass
class RowSequence:
    """
    A class to represent a stitch and quantity
    """
    stitch: Stitch
    n_stitches: int
    color_change: bool

    def __post_init__(self):
        if self.n_stitches < 0:
            raise ValueError("Number of stitches must be positive")


if __name__ == '__main__':
    from database import StitchDatabase
    from region import Region

    stitch = StitchDatabase().load_stitch(id=1, region=Region('UK'))
    row_sequence = RowSequence(stitch, 5, False)
    print(row_sequence)
