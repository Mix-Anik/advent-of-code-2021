from typing import List


def part_1(data: List[str]):
    row_length = len(data[0])
    mcb = ''
    lcb = ''

    for col_idx in range(row_length):
        col_bits = [line[col_idx] for line in data]
        col_mcb, col_lcb = calc_mcb_and_lcb(col_bits)
        mcb += col_mcb
        lcb += col_lcb

    return int(lcb, 2) * int(mcb, 2)


def part_2(data: List[str]):
    o2gr_data = co2sr_data = data
    o2gr = co2sr = '-1'

    for col_num in range(0, len(data[0])):
        o2gr_bits = [line[col_num] for line in o2gr_data]
        o2gr_bit, _ = calc_mcb_and_lcb(o2gr_bits)
        o2gr_data = [line for line in o2gr_data if line[col_num] == o2gr_bit]

        if len(o2gr_data) == 1:
            o2gr = o2gr_data[0]

        co2sr_bits = [line[col_num] for line in co2sr_data]
        _, co2sr_bit = calc_mcb_and_lcb(co2sr_bits)
        co2sr_data = [line for line in co2sr_data if line[col_num] == co2sr_bit]

        if len(co2sr_data) == 1:
            co2sr = co2sr_data[0]

    return int(co2sr, 2) * int(o2gr, 2)


def calc_mcb_and_lcb(bits: List[str]):
    # calculate most / least common bits
    bits_sum = sum([int(bit) for bit in bits])
    bits_hl = len(bits) / 2

    if bits_sum >= bits_hl:
        return '1', '0'
    else:
        return '0', '1'
