import re
from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, List

from .patterns import UK_PATTERNS


class InvalidPostcodeError(Exception):
    def __init__(self):
        Exception.__init__(self, "The postcode provided is invalid.")


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
        if not self.is_valid:
            raise InvalidPostcodeError()

        return re.findall(
            r"^((([A-Z][A-Z]{0,1})([0-9][A-Z0-9]{0,2})) {0,}(([0-9])([A-Z]{2})))",
            self.postcode,
        )[0]

    @property
    def components(self) -> Dict[str, str]:
        components = [component.name for component in list(Component)]
        *(c, o, a, *d), i, s, u = self.explode()  # pylint: disable=invalid-name

        district_detail = [
            "".join([s for s in d[0] if s.isdigit()]),
            "".join([s for s in d[0]] if any(s.isalpha() for s in d[0]) else "N/A"),
        ]

        return dict(zip(components, [c, o, a, *district_detail, i, s, u]))
