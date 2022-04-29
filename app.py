import json
import os

import postcodes as pc

PATTERNS = [
    "AA9a 9aa",
    "B9b 9bb",
    "C9 9cc",
    "D99 9dd",
    "EE9 9ee",
    "FF99 9ff",
]


def main() -> None:

    print(
        *[json.dumps(pc.Postcode(p).components, indent=4) for p in PATTERNS],
        sep="\n",
    )


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
