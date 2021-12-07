import logging

from inputs import get_file_data
from days.day_7 import solution


LOG = logging.getLogger()


class TestDay7Solutions:

    def setup_class(self):
        self.test_day_7_data = get_file_data('input_day7_test', False).strip('\n')
        self.day_7_data = get_file_data('input_day7', False).strip('\n')

    def test_part_1(self):
        assert solution(self.test_day_7_data, True) == 37

    def test_part_2(self):
        assert solution(self.test_day_7_data, False) == 168

    def teardown_class(self):
        LOG.info(f'Part 1 answer: {solution(self.day_7_data, True)}')  # 335271
        LOG.info(f'Part 2 answer: {solution(self.day_7_data, False)}')  # 95851339

