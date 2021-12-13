from typing import List, Tuple


def part_1(data: List[str]):
    paper_dots = [tuple(int(n) for n in x.split(',')) for x in data[0].splitlines()]
    fold_instructions = [x[11:].split('=') for x in data[1].splitlines()][:1]

    return len(fold_paper(paper_dots, fold_instructions))


def part_2(data: List[str]):
    paper_dots = [tuple(int(n) for n in x.split(',')) for x in data[0].splitlines()]
    fold_instructions = [x[11:].split('=') for x in data[1].splitlines()]
    paper_dots = fold_paper(paper_dots, fold_instructions)
    xmax = max([dot[0] for dot in paper_dots]) + 1
    ymax = max([dot[1] for dot in paper_dots]) + 1
    display = [['.' for _ in range(xmax)] for _ in range(ymax)]

    for x, y in paper_dots:
        display[y][x] = '▋'

    return '\n'.join([''.join(line) for line in display])


def fold_paper(paper_dots: List[Tuple[int]], fold_instructions: List[List[str]]):
    for axis, axis_val in fold_instructions:
        axis_val = int(axis_val)
        axis_idx = int(axis == 'y')
        new_dots = paper_dots.copy()

        for dot in paper_dots:
            if dot[axis_idx] > axis_val:
                new_dots.remove(dot)
                new_axis_val = axis_val - (dot[axis_idx] - axis_val)
                new_dot = (dot[1 - axis_idx], new_axis_val)
                new_dots.append(new_dot if axis_idx else new_dot[::-1])

        paper_dots = new_dots

    return set(paper_dots)
