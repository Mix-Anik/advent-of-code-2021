from typing import List, Dict, Tuple
from math import prod


def part_1(data: List[str]):
    risk_level_sum = 0
    heightmap = {(x, y): int(col) for y, row in enumerate(data) for x, col in enumerate(row)}

    for (x, y), val in heightmap.items():
        neighbours = [x for x in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)] if x in heightmap]

        if all([heightmap[p] > val for p in neighbours]):
            risk_level_sum += val + 1

    return risk_level_sum


def part_2(data: List[str]):
    basin_sizes = []
    heightmap = {(x, y): int(col) for y, row in enumerate(data) for x, col in enumerate(row)}

    for (x, y), val in heightmap.items():
        neighbours = [x for x in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)] if x in heightmap]

        if all([heightmap[p] > val for p in neighbours]):
            points = set(find_basin_points(x, y, heightmap))
            basin_sizes.append(len(points))

    return prod(sorted(basin_sizes)[-3:])


def find_basin_points(x: int, y: int, heightmap: Dict[Tuple[int, int], int]):
    basin_points = [(x, y)]
    neighbours = [x for x in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)] if x in heightmap]

    if heightmap[(x, y)] == 9:
        return []

    for (i, j) in neighbours:
        if heightmap[(i, j)] > heightmap[(x, y)]:
            basin_points.extend(find_basin_points(i, j, heightmap))

    return basin_points
