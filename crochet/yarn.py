from dataclasses import dataclass
from typing import Literal


@dataclass
class Weight:
    """
    Class to represent a yawns weight.
    Acceptable metrics are 'yards' and 'grams'
    """
    amount: float
    unit: Literal['yards', 'grams'] = 'yards'
    _units = ['yards', 'grams']

    def __post_init__(self):
        if self.unit not in self._units:
            raise ValueError(f'Unit must be one of: {", ".join(str(x) for x in self._units)}')


@dataclass
class Yarn:
    """
    Class to represent yarn
    """
    brand: str
    color: str
    weight: Weight


if __name__ == '__main__':
    yarn = Yarn('Yarn maker', 'red', Weight(200, 'gram'))
    print(yarn)