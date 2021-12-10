import collections
from typing import List


def part_1(data: List[str]):
    oc = {'(': ')', '[': ']', '{': '}', '<': '>'}
    char_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score = 0

    for line in data:
        errors = ''
        deque = collections.deque([line[0]])
        line = line[1:]

        while deque and len(line):
            if line[0] in '([{<':
                deque.append(line[0])
            else:
                start = deque.pop()
                if line[0] != oc[start]:
                    errors += line[0]

            line = line[1:]

        if errors:
            score += char_scores[errors[0]]

    return score


def part_2(data: List[str]):
    oc = {'(': ')', '[': ']', '{': '}', '<': '>'}
    char_scores = {')': 1, ']': 2, '}': 3, '>': 4}
    scores = []

    for line in data:
        start_chars = collections.deque([])
        score = 0
        has_errors = False

        while len(line):
            if line[0] in '([{<':
                start_chars.append(line[0])
            else:
                start = start_chars.pop()
                if line[0] != oc[start]:
                    has_errors = True
                    break

            line = line[1:]

        if has_errors:
            continue

        not_closed = ''.join(start_chars)[::-1]

        for char in not_closed:
            score = score * 5 + char_scores[oc[char]]

        scores.append(score)

    return sorted(scores)[int(len(scores) / 2)]
