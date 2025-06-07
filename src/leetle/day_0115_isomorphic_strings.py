import unittest
import itertools
from collections import Counter
from dataclasses import dataclass


@dataclass(frozen=True)
class CharGroup:
    char: str
    count: int

def count(s):
    return [
        CharGroup(key, len(list(group)))
        for key, group in itertools.groupby(s)
    ]


def solve(s, t):
    s_groups = count(s)
    t_groups = count(t)

    if len(s_groups) != len(t_groups):
        return False

    s_map = {}
    t_map = {}
    for s_group, t_group in zip(s_groups, t_groups):
        if s_group.count != t_group.count:
            return False
        if (
            (s_map_val := s_map.get(s_group.char))
            is not None
            and s_map_val != t_group.char
        ):
            return False
        if (
            (t_map_val := t_map.get(t_group.char))
            is not None
            and t_map_val != s_group.char
        ):
            return False
        s_map[s_group.char] = t_group.char
        t_map[t_group.char] = s_group.char
    return True


class TestDay115(unittest.TestCase):

    def test_leetle_case_1(self):
        self.assertEqual(solve("egg", "add"), True)

    def test_leetle_case_2(self):
        self.assertEqual(solve("foo", "bar"), False)

    def test_leetle_case_3(self):
        self.assertEqual(solve("paper", "title"), True)

    def test_leetle_case_4(self):
        self.assertEqual(solve("", ""), True)

    def test_leetle_case_5(self):
        self.assertEqual(solve("badc", "baba"), False)

    def test_leetle_case_6(self):
        self.assertEqual(solve("a", "b"), True)
        
    def test_same_counts_wrong_order(self):
        self.assertEqual(solve("abb", "ccd"), False)


if __name__ == "__main__":
    # use below if running in Jupyter
    # unittest.main(argv=[''], exit=False)
    unittest.main()