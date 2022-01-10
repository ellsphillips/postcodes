import os

from postcodes import Postcode

PATTERNS = [
    "AA9A 9AA",
    "B9B 9BB",
    "C9 9CC",
    "D99 9DD",
    "EE9 9EE",
    "FF9F 9FF",
    "GG99 9GG",
]


def main() -> None:

    register = {code: Postcode(code) for code in PATTERNS}

    print(*[pc.is_valid for pc in register.values()], sep="\n")


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
