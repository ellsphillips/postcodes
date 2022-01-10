import re
from dataclasses import dataclass
from enum import Enum, auto

from .patterns import UK_PATTERNS


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

    @property
    def is_valid(self) -> bool:
        pattern = re.compile(UK_PATTERNS["simple"])
        return bool(re.match(pattern, self.postcode))

    def _parse(self) -> None:
        self.postcode = self.postcode.replace(" ", "").upper()
