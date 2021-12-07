def solution(data: str, const_inc: bool):
    crabs = [int(num) for num in data.split(',')]
    fuel_amounts = []

    for num in range(min(crabs), max(crabs) + 1):
        fuel_spent = 0

        for crab_pos in crabs:
            if not const_inc:
                diff = abs(crab_pos - num)
                fuel_spent += int(diff * (diff + 1) / 2)
            else:
                fuel_spent += abs(crab_pos - num)

        fuel_amounts.append(fuel_spent)

    return min(fuel_amounts)
