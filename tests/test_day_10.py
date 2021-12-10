import logging

from inputs import get_file_data
from days.day_10 import part_1, part_2


LOG = logging.getLogger()


class TestDay10Solutions:

    def setup_class(self):
        self.test_day_10_data = get_file_data('input_day10_test')
        self.day_10_data = get_file_data('input_day10')

    def test_part_1(self):
        assert part_1(self.test_day_10_data) == 26397

    def test_part_2(self):
        assert part_2(self.test_day_10_data) == 288957

    def teardown_class(self):
        LOG.info(f'Part 1 answer: {part_1(self.day_10_data)}')  # 389589
        LOG.info(f'Part 2 answer: {part_2(self.day_10_data)}')  # 1190420163

