from typing import Tuple
import re


def part_1(data: str):
    x_interval, y_interval = [(int(a), int(b)) for a,b in re.findall('(-?\d+)\.\.(-?\d+)', data)]
    y_max_vel = abs(y_interval[0]) - 1

    return int(y_max_vel * (y_max_vel + 1) / 2)


def part_2(data: str):
    x_interval, y_interval = [(int(a), int(b)) for a,b in re.findall('(-?\d+)\.\.(-?\d+)', data)]
    target_points = [(x, y) for x in range(x_interval[0], x_interval[1] + 1) for y in range(y_interval[0], y_interval[1] + 1)]
    setups_to_try = [(x, y) for x in range(x_interval[1] + 1) for y in range(y_interval[0], y_interval[0] * -1)]
    valid_setups = []

    for point in target_points:
        for setup in setups_to_try:
            is_hit = simulate_hit(setup, point)

            if is_hit:
                valid_setups.append(setup)

    return len(set(valid_setups))


def simulate_hit(velocity: Tuple[int, int], target: Tuple[int, int]):
    pos = (0, 0)

    while True:
        pos = (pos[0] + velocity[0], pos[1] + velocity[1])
        velocity = (0 if not velocity[0] else velocity[0] - 1, velocity[1] - 1)

        if pos == target:
            return True

        if pos[0] > target[0] or pos[1] < target[1]:
            return False
