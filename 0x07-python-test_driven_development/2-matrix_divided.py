def matrix_divided(matrix, div):
    """ The body of the method """
    if not all(isinstance(row, list) and
               all(isinstance(i, (int, float))
                   for i in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    for row in range(len(matrix) - 1):
        if len(matrix[row]) != len(matrix[row + 1]):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    main_mat = []

    for row in matrix:
        new_mat = []
        for i in row:
            new_mat.append(round(i / div, 2))
        main_mat.append(new_mat)

    return main_mat
