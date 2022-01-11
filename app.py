import json
import os

from postcodes import Postcode

PATTERNS = [
    "AA9a9aa",
    "B9b9bb",
    "C99cc",
    "D999dd",
    "EE99ee",
    "FF999ff",
]


def main() -> None:

    print(json.dumps(Postcode(PATTERNS[0]).components, indent=4))


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
