
def normalize_codes(codes: list[str]) -> list[str]:
    return [code.replace(" ", "") for code in codes]


codes = ["dsa", "abc", "qet", "abc dsad"]
codes = normalize_codes(codes)