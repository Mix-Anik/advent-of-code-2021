from typing import List


def part_1(data: List[List[str]]):
    occurrences = 0

    for row in data:
        occurrences += len([val for val in row[1].split() if len(val) in [2, 3, 4, 7]])

    return occurrences


def part_2(data: List[List[str]]):
    outputs_sum = 0

    for row in data:
        encoding = find_encoding(row[0].split())
        num = int(''.join([encoding[''.join(sorted(pattern))] for pattern in row[1].split() if ''.join(sorted(pattern)) in encoding]))
        outputs_sum += num

    return outputs_sum


def find_encoding(patterns: List[str]):
    encoding = {}
    # finds difference between two strings
    diff = lambda x, y: list(set(x).symmetric_difference(set(y)))
    # finds first pattern that has string difference of 'd' with given one
    fnp = lambda x, y, d: next(filter(lambda z: len(diff(z, y)) == d, x))

    # adding numbers we can distinguish right away due to unique length
    for p in patterns:
        length = len(p)

        if length == 2:
            encoding[1] = p
        elif length == 4:
            encoding[4] = p
        elif length == 3:
            encoding[7] = p
        elif length == 7:
            encoding[8] = p

    # track patterns which haven't been found, so there wouldn't be unexpected collisions
    yet_to_find = [n for n in patterns if n not in encoding.values()]

    # finding top segment char by finding difference between number 1 and 7 patterns
    t = diff(encoding[1], encoding[7])[0]
    # finding number 9 pattern as it has a difference of 1 with number 4's pattern concatenated with top segment char
    encoding[9] = fnp(yet_to_find, encoding[4] + t, 1)
    # remove number 9's pattern from yet_to_find, so there wouldn't be unexpected collisions
    yet_to_find.remove(encoding[9])
    # further logic is identical the one described above

    b = diff(encoding[4] + t, encoding[9])[0]
    encoding[3] = fnp(yet_to_find, encoding[7] + b, 1)
    yet_to_find.remove(encoding[3])

    encoding[5] = fnp(yet_to_find, encoding[9], 1)
    yet_to_find.remove(encoding[5])

    bl = diff(encoding[8], encoding[9])[0]
    encoding[6] = fnp(yet_to_find, encoding[5] + bl, 0)
    yet_to_find.remove(encoding[6])

    encoding[0] = fnp(yet_to_find, encoding[8], 1)
    yet_to_find.remove(encoding[0])

    encoding[2] = yet_to_find[0]

    return {''.join(sorted(v)): str(k) for k, v in encoding.items()}

