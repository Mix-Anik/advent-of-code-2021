from typing import List, Tuple


def part_1(data: List[Tuple[str, int]]):
    pos = [0, 0]

    for (direction, step) in data:
        if direction == 'forward':
            pos[0] += step
        elif direction == 'up':
            pos[1] -= step
        elif direction == 'down':
            pos[1] += step

    return pos[0] * pos[1]


def part_2(data: List[Tuple[str, int]]):
    pos = [0, 0, 0]

    for (direction, step) in data:
        if direction == 'forward':
            pos[0] += step
            pos[1] += pos[2] * step
        elif direction == 'up':
            pos[2] -= step
        elif direction == 'down':
            pos[2] += step

    return pos[0] * pos[1]
