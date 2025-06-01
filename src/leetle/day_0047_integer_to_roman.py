import enum


class RomanNums(enum.Enum):
    ONE = "I"
    FIVE = "V"
    TEN = "X"
    FIFTY = "L"
    HUNDRED = "C"
    FIVE_HUNDRED = "D"
    THOUSAND = "M"


def digit(val, sym_one, sym_five, sym_ten):
    if val <= 3:
        return val * sym_one
    if val == 4:
        return sym_one + sym_five
    if 5 <= val <= 8:
        return sym_five + (val - 5) * sym_one
    if val == 9:
        return sym_one + sym_ten


def solve(num):
    assert 0 < num < 4000
    num_str = str(num).zfill(4)
    return (
        int(num_str[0]) * RomanNums.THOUSAND.value
        + digit(
            int(num_str[1]),
            RomanNums.HUNDRED.value,
            RomanNums.FIVE_HUNDRED.value,
            RomanNums.THOUSAND.value,
        )
        + digit(
            int(num_str[2]),
            RomanNums.TEN.value,
            RomanNums.FIFTY.value,
            RomanNums.HUNDRED.value,
        )
        + digit(
            int(num_str[3]),
            RomanNums.ONE.value,
            RomanNums.FIVE.value,
            RomanNums.TEN.value,
        )
    )
