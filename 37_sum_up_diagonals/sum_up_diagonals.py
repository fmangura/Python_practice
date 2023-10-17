m1 = [
        [1,   2],
        [30, 40],
    ]

m2 = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
         ]

def sum_up_diagonals(matrix):

    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    sum1 = 0
    sum2 = 0
    for i in range(len(matrix)):
        sum1 = sum1 + matrix[i][i]
        print(sum1)
    
    for i in range(len(matrix)):
        sum2 = sum2 + matrix[i][len(matrix) - i - 1]
        print(sum2)

    return sum1 + sum2




    # return sum([sum(list) for list in matrix])