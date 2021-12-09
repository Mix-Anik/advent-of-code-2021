import logging

from inputs import get_file_data
from days.day_9 import part_1, part_2


LOG = logging.getLogger()


class TestDay9Solutions:

    def setup_class(self):
        self.test_day_9_data = get_file_data('input_day9_test')
        self.day_9_data = get_file_data('input_day9')

    def test_part_1(self):
        assert part_1(self.test_day_9_data) == 15

    def test_part_2(self):
        assert part_2(self.test_day_9_data) == 1134

    def teardown_class(self):
        LOG.info(f'Part 1 answer: {part_1(self.day_9_data)}')  # 518
        LOG.info(f'Part 2 answer: {part_2(self.day_9_data)}')  # 949905

