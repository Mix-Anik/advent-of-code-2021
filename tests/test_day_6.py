import logging

from inputs import get_file_data
from days.day_6 import solution


LOG = logging.getLogger()


class TestDay6Solutions:

    def setup_class(self):
        self.test_day_6_data = get_file_data('input_day6_test', False).strip('\n')
        self.day_6_data = get_file_data('input_day6', False).strip('\n')

    def test_part_1(self):
        assert solution(self.test_day_6_data, 80) == 5934

    def test_part_2(self):
        assert solution(self.test_day_6_data, 256) == 26984457539

    def teardown_class(self):
        LOG.info(f'Part 1 answer: {solution(self.day_6_data, 80)}')  # 350149
        LOG.info(f'Part 2 answer: {solution(self.day_6_data, 256)}')  # 1590327954513

