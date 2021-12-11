import logging

from inputs import get_file_data
from days.day_8 import part_1, part_2


LOG = logging.getLogger()


class TestDay8Solutions:

    def setup_class(self):
        self.test_day_8_data = [data.split(' | ') for data in get_file_data('input_day8_test')]
        self.day_8_data = [data.split(' | ') for data in get_file_data('input_day8')]

    def test_part_1(self):
        assert part_1(self.test_day_8_data) == 26

    def test_part_2(self):
        assert part_2(self.test_day_8_data) == 61229

    def teardown_class(self):
        LOG.info(f'Part 1 answer: {part_1(self.day_8_data)}')  # 303
        LOG.info(f'Part 2 answer: {part_2(self.day_8_data)}')  # 961734

