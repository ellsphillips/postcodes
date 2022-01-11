import re
from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, List

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
        _postcode = self.postcode.replace(" ", "").upper()
        self.postcode = " ".join([_postcode[:-3], _postcode[-3:]])

    def explode(self) -> List[str]:
        return re.findall(
            r"^((([A-Z][A-Z]{0,1})([0-9][A-Z0-9]{0,2})) {0,}(([0-9])([A-Z]{2})))",
            self.postcode,
        )[0]

    @property
    def components(self) -> Dict[str, str]:
        components = [component.name for component in list(Component)]
        explosion = self.explode()

        shrapnel = [
            explosion[0],
            explosion[1],
            explosion[2],
            "".join([s for s in explosion[3] if s.isdigit()]),
            "".join(
                [s for s in explosion[3]]
                if any(s.isalpha() for s in explosion[3])
                else "N/A"
            ),
            explosion[4],
            explosion[5],
            explosion[6],
        ]

        return dict(zip(components, shrapnel))
