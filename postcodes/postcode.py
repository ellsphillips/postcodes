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

    def explode(self):
        comps = [component.name for component in list(Component)]

        parts = list(
            re.findall(
                r"^((([A-Z][A-Z]{0,1})([0-9][A-Z0-9]{0,2})) {0,}(([0-9])([A-Z]{2})))",
                self.postcode,
            )
        )

        return zip(comps, *parts)
