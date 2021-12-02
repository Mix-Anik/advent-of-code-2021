import logging

from inputs import get_file_data
from days.day_2 import part_1, part_2


LOG = logging.getLogger()


class TestDay2Solutions:

    def setup_class(self):
        test_commands = [line.split() for line in get_file_data('input_day2_test')]
        commands = [line.split() for line in get_file_data('input_day2')]
        self.test_day_2_data = [(cmd[0], int(cmd[1])) for cmd in test_commands]
        self.day_2_data = [(cmd[0], int(cmd[1])) for cmd in commands]

    def test_part_1(self):
        assert part_1(self.test_day_2_data) == 150

    def test_part_2(self):
        assert part_2(self.test_day_2_data) == 900

    def teardown_class(self):
        LOG.info(f'Part 1 answer: {part_1(self.day_2_data)}')  # 1383564
        LOG.info(f'Part 2 answer: {part_2(self.day_2_data)}')  # 1488311643
