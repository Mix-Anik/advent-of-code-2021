import logging

from inputs import get_file_data
from days.day_4 import part_1, part_2


LOG = logging.getLogger()


def prepare_data(data):
    order_data = [int(num) for num in data[0].split(',')]
    boards_data = data[2:] + ['']
    boards = []
    cur_board = []

    for line in boards_data:
        if line == '':
            boards.append(cur_board)
            cur_board = []
            continue

        cur_board.append([int(num) for num in line.split()])

    return order_data, boards


class TestDay4Solutions:

    def setup_class(self):
        self.test_day_4_data = get_file_data('input_day4_test')
        self.day_4_data = get_file_data('input_day4')

    def test_part_1(self):
        order, boards = prepare_data(self.test_day_4_data)
        assert part_1(order, boards) == 4512

    def test_part_2(self):
        order, boards = prepare_data(self.test_day_4_data)
        assert part_2(order, boards) == 1924

    def teardown_class(self):
        order, boards = prepare_data(self.day_4_data)
        LOG.info(f'Part 1 answer: {part_1(order, boards)}')  # 44088
        LOG.info(f'Part 2 answer: {part_2(order, boards)}')  # 23670

