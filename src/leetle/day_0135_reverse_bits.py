def solve(n):
    # assume n fits inside uint32
    n_bin_u32 = f"{n:b}".zfill(32)
    return int(n_bin_u32[::-1], base=2)
