def clean_room(grid, start):
    rows = len(grid)
    cols = len(grid[0])

    visited = set()
    stack = [start]

    while stack:
        row, column = stack.pop()

        if (row, column) in visited or grid[row][column] == 1:
            continue
        visited.add((row, column))

        for next_row, next_column in [(0,-1), (-1, 0), (0, 1), (1, 0)]:
            new_row = row+next_row
            new_column = column+next_column

            if 0<=new_row<rows and 0<=new_column<cols:
                stack.append((new_row, new_column))

    return len(visited)

room = [
 [0, 1, 0, 1, 0],
 [1, 1, 0, 1, 0],
 [1, 1, 0, 0, 0],
 [0, 0, 0, 0, 0]
]

start_position = (3, 0)

print(clean_room(room, start_position))