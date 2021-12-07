def solution(data: str, days_to_simulate: int):
    cycles = [int(num) for num in data.split(',')]
    cycle_counts = {i: cycles.count(i) for i in range(9)}

    for i in range(days_to_simulate):
        zero_day_cycle_count = cycle_counts[0]

        for day in range(1, 9):
            cycle_counts[day - 1] = cycle_counts[day]

        cycle_counts[8] = zero_day_cycle_count
        cycle_counts[6] += zero_day_cycle_count

    return sum(cycle_counts.values())
