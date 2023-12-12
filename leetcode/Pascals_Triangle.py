def pascals_triangle(numRows):
    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1], [1, 1]]
    else:
        triangle = [[1], [1, 1]]
        for opa in range(numRows - 2):
            new = []
            top = triangle[-1] #use triangle[-1] instead of top to save memory
            for i in range(len(top) - 1):
                new.append(top[i] + top[i + 1])
            triangle.append([1] + new + [1])
    return triangle

pascals_triangle(5)

