from pathlib import Path

import pandas as pd

from region import Region
from stitch import Stitch


class StitchDatabase:

    def __init__(self):
        csv_path = Path(__file__).parent / 'resources/stitch_lookup.csv'
        self.stitches = pd.read_csv(csv_path)

    def load_stitch(self, id: int, region: Region) -> Stitch:
        """
        Loads a stitch based on ID and region
        :param id:
        :param region:
        :return:
        """
        stitch_raw = self.stitches[
            (self.stitches['id'] == id) &
            (self.stitches['region'] == region.region)
            ]

        stitch = Stitch(
            id=stitch_raw.id,
            term=stitch_raw.term,
            symbol=stitch_raw.symbol,
            region=region,
        )

        return stitch
