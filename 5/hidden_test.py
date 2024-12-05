import unittest
import pytest
from my_utils import read_aoc_data
from problem import part_a, part_b

class Tests(unittest.TestCase):
    # update with correct solution answers post-implementation
    part_a_answer = 0
    part_b_answer = 0

    # update with correct day and year
    aoc_day = 'X'
    aoc_year = 2023

    @pytest.mark.timeout(10)
    def test_part_a(self):
        result = part_a(read_aoc_data(self.aoc_day, self.aoc_year))
        self.assertEqual(result, self.part_a_answer)

    @pytest.mark.timeout(10)
    def test_part_b(self):
        result = part_b(read_aoc_data(self.aoc_day, self.aoc_year))
        self.assertEqual(result, self.part_b_answer)

if __name__ == '__main__':
    unittest.main()