from typing import List


def part_1(order: List[int], boards: List[List[List[int]]]):
    marked_nums = []

    for num in order:
        marked_nums.append(num)

        for board in boards:
            if board_has_won(board, marked_nums):
                return num * board_sum(board, marked_nums)

    return -1


def part_2(order: List[int], boards: List[List[List[int]]]):
    marked_nums = []
    boards_won = []
    latest_winning_num = None

    for num in order:
        marked_nums.append(num)

        for idx, board in enumerate(boards):
            if board_has_won(board, marked_nums) and idx not in boards_won:
                boards_won.append(idx)
                latest_winning_num = num

    latest_winning_board = boards[boards_won[-1]]
    return latest_winning_num * board_sum(latest_winning_board, marked_nums[:marked_nums.index(latest_winning_num) + 1])


def board_has_won(board: List[List[int]], marked_nums: List[int]):
    for row in board:
        if all([num in marked_nums for num in row]):
            return True

    for col_idx in range(len(board[0])):
        col = [line[col_idx] for line in board]

        if all([num in marked_nums for num in col]):
            return True

    return False


def board_sum(board: List[List[int]], marked_nums: List[int]):
    nums_to_sum = []

    for row in board:
        for num in row:
            if num not in marked_nums:
                nums_to_sum.append(num)

    return sum(nums_to_sum)
