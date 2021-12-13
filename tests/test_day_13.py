import logging

from inputs import get_file_data
from days.day_13 import part_1, part_2


LOG = logging.getLogger()


class TestDay13Solutions:

    def setup_class(self):
        self.test_day_13_data = get_file_data('input_day13_test', False).split('\n\n')
        self.day_13_data = get_file_data('input_day13', False).split('\n\n')

    def test_part_1(self):
        assert part_1(self.test_day_13_data) == 17

    def teardown_class(self):
        LOG.info(f'Part 1 answer: {part_1(self.day_13_data)}')  # 785
        LOG.info(f'Part 2 answer:\n{part_2(self.day_13_data)}')  # FJAHJGAH

