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

    register = {code: Postcode(code) for code in PATTERNS}

    print(*[pc.is_valid for pc in register.values()], sep="\n")


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
