from pathlib import Path

import pandas as pd

from region import Region


class Stitch:
    """
    Class to represent a crochet stitch.
    """

    def __init__(self):
        csv_path = Path(__file__).parent / 'resources/stitch_lookup.csv'
        self._stitches = pd.read_csv(csv_path)

    def load_stitch(self, id: int, region: Region):
        """

        :param id: Unique stitch identifier
        """
        stitch = self._stitches[
            (self._stitches['id'] == id) &
            (self._stitches['region'] == region.region)
            ]
        self.id = stitch.id
        self.term = stitch.term
        self.symbol = stitch.symbol
        self.region = region.region

    def create_stitch(
            self,
            term: str,
            symbol: str,
            region: Region,
            existing: bool = True
    ):
        """
        Creates a new stitch with a new id and writes to local db

        :param term: Detailed name of stitch
        :param symbol: Short form name used within a pattern
        :param region: Region that terms are associated with
        :param existing: If true, will load from database and only name is required
        """
        pass


    def change_region(self):
        """
        Switches the current region.
        E.g. is currently US it will switch to UK
        """
        return


if __name__ == '__main__':
    db = Stitch()
    db.load_stitch(1, Region('UK'))
    print(db.__dict__)
