from dataclasses import dataclass


@dataclass
class Region:
    """
    Class to represent a region.
    Acceptable metrics are 'US' and 'UK'
    """
    region: str
    _regions = ['US', 'UK']

    def __post_init__(self):
        if self.region not in self._regions:
            raise ValueError(f'Region must be one of: {", ".join(str(x) for x in self._regions)}')


if __name__ == '__main__':
    print(Region('UL'))
