def rotate(matrix) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    matrix.reverse()
    index_to_replace = 1
    for i in range(len(matrix)):
        for v in range(index_to_replace, len(matrix)):
            matrix[i][v], matrix[v][i] = matrix[v][i], matrix[i][v]
        index_to_replace += 1

    #for assertions only!!!
    return matrix

assert rotate([[1,2,3],[4,5,6],[7,8,9]]) == [[7,4,1],[8,5,2],[9,6,3]]
assert rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]) == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]