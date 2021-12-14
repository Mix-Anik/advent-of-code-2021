import logging

from inputs import get_file_data
from days.day_14 import part_1, part_2


LOG = logging.getLogger()


class TestDay14Solutions:

    def setup_class(self):
        self.test_day_14_data = get_file_data('input_day14_test', False).split('\n\n')
        self.day_14_data = get_file_data('input_day14', False).split('\n\n')

    def test_part_1(self):
        assert part_1(self.test_day_14_data) == 1588

    def test_part_2(self):
        assert part_2(self.test_day_14_data) == 2188189693529

    def teardown_class(self):
        LOG.info(f'Part 1 answer: {part_1(self.day_14_data)}')  # 3095
        LOG.info(f'Part 2 answer: {part_2(self.day_14_data)}')  # 3152788426516

