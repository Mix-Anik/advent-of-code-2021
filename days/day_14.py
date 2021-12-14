from typing import List, Dict


def part_1(data: List[str]):
    template = data[0]
    rules = dict([tuple(x.split(' -> ')) for x in data[1].splitlines()])
    counts = []

    for i in range(10):
        template = step(template, rules)

    for c in set(template):
        counts.append(template.count(c))

    return max(counts) - min(counts)


def part_2(data: List[str]):
    template = data[0]
    rules = dict([tuple(x.split(' -> ')) for x in data[1].splitlines()])
    pair_counts = {pair: 0 for pair in rules}
    char_counts = {}

    for i in range(len(template) - 1):
        pair_counts[template[i:i + 2]] += 1

    for i in range(40):
        new_pair_counts = {pair: 0 for pair in rules}

        for pair, count in pair_counts.items():
            ins = rules[pair]
            new_pair_counts[pair[0] + ins] += count
            new_pair_counts[ins + pair[1]] += count

        pair_counts = new_pair_counts

    for pair, count in pair_counts.items():
        char_counts[pair[0]] = char_counts.get(pair[0], 0) + count

    char_counts[template[-1]] += 1

    return max(char_counts.values()) - min(char_counts.values())


def step(template: str, rules: Dict[str, str]):
    new_template = ''

    for i in range(len(template) - 1):
        pair = template[i:i + 2]
        new_template += f'{rules[pair]}{pair[1]}' if i > 0 else f'{pair[0]}{rules[pair]}{pair[1]}'

    return new_template
