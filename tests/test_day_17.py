import logging
import pytest

from days.day_17 import part_1, part_2


LOG = logging.getLogger()


class TestDay17Solutions:

    def setup_class(self):
        self.test_day_17_data = 'target area: x=20..30, y=-10..-5'
        self.day_17_data = 'target area: x=60..94, y=-171..-136'

    def test_part_1(self):
        assert part_1(self.test_day_17_data) == 45
        LOG.info(f'Part 1 answer: {part_1(self.day_17_data)}')  # 14535

    @pytest.mark.skip(reason="very slow")
    def test_part_2(self):
        assert part_2(self.test_day_17_data) == 112
        LOG.info(f'Part 2 answer: {part_2(self.day_17_data)}')  # 2270

