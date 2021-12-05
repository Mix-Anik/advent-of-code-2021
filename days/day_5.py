from typing import List


def part_1(data: List[str], diagonals=False):
    segments = [line.split(' -> ') for line in data]
    points_dict = {}

    for seg in segments:
        for point in get_segment_points(seg, diagonals):
            points_dict[point] = points_dict.get(point, 0) + 1

    return sum([value > 1 for value in points_dict.values()])


def part_2(data: List[str]):
    return part_1(data, True)


def get_segment_points(seg_points: List[str], diagonals=False):
    points = []
    p1, p2 = seg_points[0].split(','), seg_points[1].split(',')
    x1, y1, x2, y2 = map(int, p1 + p2)
    dx, dy = abs(x1 - x2), abs(y1 - y2)

    if dx and dy and not diagonals:
        return []
    elif dx and dy and diagonals:
        length = abs(x1 - x2) + 1

        if x1 > x2:
            if y1 > y2:
                points += [(x1 - i, y1 - i) for i in range(length)]
            else:
                points += [(x1 - i, y1 + i) for i in range(length)]
        else:
            if y1 > y2:
                points += [(x1 + i, y1 - i) for i in range(length)]
            else:
                points += [(x1 + i, y1 + i) for i in range(length)]
    elif dx:
        xmin = min(x1, x2)
        points += [(i, y1) for i in range(xmin, xmin + dx + 1)]
    else:
        ymin = min(y1, y2)
        points += [(x1, i) for i in range(ymin, ymin + dy + 1)]

    return points
