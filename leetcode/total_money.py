def totalMoney(n):
    full_weeks = n // 7
    remaining = n - full_weeks * 7
    days = []
    for i in range(0, full_weeks):
        days=days+[i+z for z in range(1, 8)]

    days = days+[full_weeks+z for z in range(1, remaining+1)]

    return sum(days)

print(totalMoney(4))