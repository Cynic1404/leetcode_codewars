def getRow(rowIndex: int):
    if rowIndex == 0:
        return [1]
    elif rowIndex == 1:
        return [1, 1]
    else:
        top = [1, 1]
        for _ in range(rowIndex - 1):
            new_row = []

            for i in range(len(top) - 1):
                new_row += [top[i] + top[i + 1]]

            top = [1] + new_row + [1]
    return top

print(getRow(3))