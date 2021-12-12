import logging

from inputs import get_file_data
from days.day_12 import part_1, part_2


LOG = logging.getLogger()


class TestDay12Solutions:

    def setup_class(self):
        self.test1_day_12_data = get_file_data('input_day12_test1')
        self.test2_day_12_data = get_file_data('input_day12_test2')
        self.test3_day_12_data = get_file_data('input_day12_test3')
        self.day_12_data = get_file_data('input_day12')

    def test_part_1(self):
        assert part_1(self.test1_day_12_data) == 10
        assert part_1(self.test2_day_12_data) == 19
        assert part_1(self.test3_day_12_data) == 226

    def test_part_2(self):
        assert part_2(self.test1_day_12_data) == 36
        assert part_2(self.test2_day_12_data) == 103
        assert part_2(self.test3_day_12_data) == 3509

    def teardown_class(self):
        LOG.info(f'Part 1 answer: {part_1(self.day_12_data)}')  # 4495
        LOG.info(f'Part 2 answer: {part_2(self.day_12_data)}')  # 131254

