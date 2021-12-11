from typing import List, Dict, Tuple
from collections import deque


def part_1(data: List[List[int]]):
    total_flashes = 0
    grid = {(x, y): col for y, row in enumerate(data) for x, col in enumerate(row)}

    for i in range(100):
        grid, total_flashes = step(grid, total_flashes)

    return total_flashes


def part_2(data: List[List[int]]):
    step_count = 0
    grid = {(x, y): col for y, row in enumerate(data) for x, col in enumerate(row)}
    grid_sum = sum(grid.values())

    while grid_sum != 0:
        grid, _ = step(grid)

        step_count += 1
        grid_sum = sum(grid.values())

    return step_count


def step(grid: Dict[Tuple[int, int], int], flashes_count: int = 0):
    for p in grid:
        grid[p] += 1

    flashing = deque([p for p, val in grid.items() if val > 9])

    while flashing:
        (x, y) = flashing.pop()
        neighbours = [p for p in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1),
                                  (x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1), (x - 1, y - 1)] if p in grid]
        grid[(x, y)] = -1
        flashes_count += 1

        for p in neighbours:
            if -1 < grid[p] < 10:
                grid[p] += 1

        flashing.extend([p for p, val in grid.items() if val > 9 and p not in flashing])

    for p in grid:
        if grid[p] == -1:
            grid[p] = 0

    return grid, flashes_count
