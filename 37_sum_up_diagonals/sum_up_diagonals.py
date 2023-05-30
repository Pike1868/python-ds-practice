import numpy as np
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
    main_diag = sum(np.diag(matrix))
    sec_diag = sum(np.diag(np.fliplr(matrix)))
    return main_diag + sec_diag
   

m1 = [
    [1,   2],
    [30, 40],
      ]

m2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(sum_up_diagonals(m1))
print(sum_up_diagonals(m2))
    