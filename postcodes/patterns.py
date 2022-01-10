KEY_PATTERNS = [
    "AA9A 9AA",
    "B9B 9BB",
    "C9 9CC",
    "D99 9DD",
    "EE9 9EE",
    "FF9F 9FF",
    "GG99 9GG",
]

UK_PATTERNS = {
    "simple": r"^([A-Z][A-HJ-Y]?\d[A-Z\d]? ?\d[A-Z]{2}|GIR ?0A{2})$",
    "complete": r"^(([A-Z]{1,2}\d[A-Z\d]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ?\d[A-Z]{2}|BFPO ?\d{1,4}|(KY\d|MSR|VG|AI)[ -]?\d{4}|[A-Z]{2} ?\d{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$",
    "overseas_terretories": r"^((ASCN|STHL|TDCU|BBND|[BFS]IQQ|GX\d{2}|PCRN|TKCA) ?\d[A-Z]{2}|(KY\d|MSR|VG|AI)[ -]?\d{4}|(BFPO|[A-Z]{2}) ?\d{2}|GE ?CX)$",
    "british_forces_post_office": r"^BFPO ?\d{1,4}$",
    "santa": r"^SAN ?TA1$",
}
