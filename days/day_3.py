from typing import List


def part_1(data: List[str]):
    gamma_rate_bits = ''

    for col_idx in range(len(data[0])):
        col_bits = [row[col_idx] for row in data]
        gamma_rate_bits += find_most_common_bit(col_bits)

    gamma_rate = int(gamma_rate_bits, 2)
    epsilon_rate = int(gamma_rate_bits.replace('1', 'x').replace('0', '1').replace('x', '0'), 2)

    return gamma_rate * epsilon_rate


def part_2(data: List[str]):
    o2_rating = find_rating(data)
    co2_rating = find_rating(data, True)

    return o2_rating * co2_rating


def find_most_common_bit(bits: List[str], least=False):
    mcb_boolean = sum([int(bit) for bit in bits]) >= len(bits) / 2

    return str(int(not mcb_boolean if least else mcb_boolean))


def find_rating(data: List[str], use_lcb=False):
    col_idx = 0

    while len(data) > 1:
        bits = [row[col_idx] for row in data]
        common_bit = find_most_common_bit(bits, use_lcb)
        data = [row for row in data if row[col_idx] == common_bit]
        col_idx += 1

    return int(data[0], 2)
