def largestLocal(grid):
    matrix_row = []
    final_matrix = []
    for row in range(len(grid[0]) - 2):
        for column in range(len(grid[0]) - 2):
            square = grid[row][column:column + 3] + grid[row + 1][column:column + 3] + grid[row + 2][column:column + 3]
            matrix_row.append(max(square))
        final_matrix.append(matrix_row)
        matrix_row = []
    return final_matrix

print(largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]))