from dataclasses import dataclass
from enum import Enum, auto


class Component(Enum):
    COMPLETE = auto()
    OUTWARD = auto()
    AREA = auto()
    DISTRICT = auto()
    SUBDISTRICT = auto()
    INWARD = auto()
    SECTOR = auto()
    UNIT = auto()


@dataclass
class Postcode:
    ...
