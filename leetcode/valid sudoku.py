def isValidSudoku(board):
    for row in board:
        filtered = list(filter(lambda x:x.isnumeric(), row))
        if len(filtered) > len(set(filtered)):
            return False

    for row in range(len(board)):
        column=[]
        for i in range(9):
            if board[i][row].isnumeric():
                column.append(board[i][row])
            if len(column) > len(set(column)):
                return False

    a,b = 0,3
    for i in range(3): #get a row of squears
        row_in_squear = 0
        column_from_squear = 3
        for column in range(3): #get 3 squears from row
            square=[]
            for row in range(a,b): #get a squear
                square += board[row][row_in_squear:column_from_squear]
            filtered = list(filter(lambda x:x.isnumeric(), square))
            if len(filtered) > len(set(filtered)):
                return False
            row_in_squear+=3
            column_from_squear+=3
        a+=3
        b+=3
    return True



print(isValidSudoku([["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","4",".",".",".",".","6","."],
  ["1",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]]))


# def isValidSudoku(board):
#     for row in range(9):
#         for cell in range(9):
#             if board[row][cell]!='.':
#                 print(f'{row}{cell}{board[row][cell]}')


# for row in range(9):
#     for cell in range(9):
#         if board[row][cell] != '.' and cell < 8:
#             for i in board[row][cell + 1:]:
#                 if board[row][cell] == i:
#                     return False