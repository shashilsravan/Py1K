from itertools import product


def hasAllCodes(s: str, k: int) -> bool:
    s1 = set([0, 1])
    for l in list(product(s1, repeat = k)):
        if s.count("".join(str(li) for li in l)) <= 0:
            return False
    return True


print(hasAllCodes("0000000001011100", 4))