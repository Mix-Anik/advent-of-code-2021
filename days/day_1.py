from typing import List


def part_1(data: List[int]):
    increases = 0
    prev = data[0]

    for num in data[1:]:
        if num > prev:
            increases += 1

        prev = num

    return increases


def part_2(data: List[int]):
    window_sums = [sum(data[i:i + 3]) for i in range(len(data) - 2)]

    return part_1(window_sums)
