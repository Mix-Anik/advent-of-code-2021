import logging

from inputs import get_file_data
from days.day_11 import part_1, part_2


LOG = logging.getLogger()


class TestDay11Solutions:

    def setup_class(self):
        self.test_day_11_data = [[int(col) for col in row] for row in get_file_data('input_day11_test')]
        self.day_11_data = [[int(col) for col in row] for row in get_file_data('input_day11')]

    def test_part_1(self):
        assert part_1(self.test_day_11_data) == 1656

    def test_part_2(self):
        assert part_2(self.test_day_11_data) == 195

    def teardown_class(self):
        LOG.info(f'Part 1 answer: {part_1(self.day_11_data)}')  # 1719
        LOG.info(f'Part 2 answer: {part_2(self.day_11_data)}')  # 232

