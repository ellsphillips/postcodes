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

    postcode: str

    def __post_init__(self) -> None:
        self._parse()

    def _parse(self) -> None:
        self.postcode = self.postcode.replace(" ", "").upper()
