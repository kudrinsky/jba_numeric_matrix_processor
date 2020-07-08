import copy


def main_menu():
    print('1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Transpose matrix')
    print('5. Calculate a determinant\n6. Inverse matrix\n0. Exit')
    user_choice = int(input('Your choice: '))
    if user_choice == 1:
        add_matrix()
    elif user_choice == 2:
        scalar_matrix()
    elif user_choice == 3:
        multiply_matrix()
    elif user_choice == 4:
        print('1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line')
        transpose(int(input('Your choice: ')))
    elif user_choice == 5:
        calculate_determinant()
    elif user_choice == 6:
        inverse_matrix()
    else:
        pass


def input_matrix(string=''):
    rows, cols = input(f'Enter size of {string}matrix: ').split()
    rows, cols = int(rows), int(cols)
    print(f'Enter {string}matrix:')
    matrix = [input().split() for i in range(rows)]
    temp = ''.join([''.join(item) for item in matrix])
    if '.' in temp:
        matrix = [[float(matrix[row][col]) for col in range(cols)] for row in range(rows)]
    else:
        matrix = [[int(matrix[row][col]) for col in range(cols)] for row in range(rows)]
    return rows, cols, matrix


def print_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    matrix = [[str(matrix[row][col]) for row in range(rows)] for col in range(cols)]
    for row in matrix:
        length = len(row[0])
        for i in range(len(row)):
            if len(row[i]) > length:
                length = len(row[i])
        for i in range(len(row)):
            if len(row[i]) < length:
                row[i] = ' ' * (length - len(row[i])) + row[i]
    rows = len(matrix)
    cols = len(matrix[0])
    matrix = [[matrix[row][col] for row in range(rows)] for col in range(cols)]
    print('The result is:')
    for row in matrix:
        for col in row:
            print(col, end=' ')
        print()


def add_matrix():
    rows1, cols1, matr_1 = input_matrix('first ')
    rows2, cols2, matr_2 = input_matrix('second ')
    if rows1 == rows2 and cols1 == cols2:
        print_matrix([[matr_1[row][col] + matr_2[row][col] for col in range(cols1)] for row in range(rows1)])
    else:
        print('The operation cannot be performed.')
    print()
    main_menu()


def scalar_matrix():
    rows, cols, matr = input_matrix()
    const = input('Enter constant: ')
    if '.' in const:
        const = float(const)
    else:
        const = int(const)
    print_matrix([[matr[row][col] * const for col in range(cols)] for row in range(rows)])
    print()
    main_menu()


def multiply_matrix():
    rows1, cols1, matr_1 = input_matrix('first ')
    rows2, cols2, matr_2 = input_matrix('second ')
    matrix = [[None for col in range(cols2)] for row in range(rows1)]
    item = 0
    if cols1 == rows2:
        for row in range(rows1):
            for col1 in range(cols2):
                for col in range(cols1):
                    item += matr_1[row][col] * matr_2[col][col1]
                matrix[row][col1] = item
                item = 0
        print_matrix(matrix)
    else:
        print('The operation cannot be performed.')
    print()
    main_menu()


def transpose(user_choice):
    rows, cols, matr = input_matrix()
    if user_choice == 1:
        print_matrix([[matr[row][col] for row in range(rows)] for col in range(cols)])
    elif user_choice == 2:
        print_matrix([[matr[row][col] for row in range(rows - 1, -1, -1)] for col in range(cols - 1, -1, -1)])
    elif user_choice == 3:
        print_matrix([item[::-1] for item in matr])
    elif user_choice == 4:
        print_matrix(matr[::-1])
    print()
    main_menu()


def calculate_determinant():
    rows, cols, matr = input_matrix()
    if rows == cols:
        print(f'The result is:\n{determinant(matr)}')
    else:
        print('The operation cannot be performed.')
    print()
    main_menu()


def reduce_matrix(matrix, i, j):
    result = copy.deepcopy(matrix)
    result.pop(i)
    for item in result:
        item.pop(j)
    return result


def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for i in range(len(matrix)):
            det += matrix[0][i] * (-1) ** (i + 2) * determinant(reduce_matrix(matrix, 0, i))
    return det


def inverse_matrix():
    rows, cols, matr = input_matrix()
    det = determinant(matr)
    if rows != cols or det == 0:
        print("This matrix doesn't have an inverse.")
    else:
        alg_matrix = [[(-1) ** (row + col + 2) * determinant(reduce_matrix(matr, row, col))
                       for row in range(rows)] for col in range(cols)]
        alg_matrix_t = [[alg_matrix[col][row] for row in range(rows)] for col in range(cols)]
        print_matrix([[alg_matrix_t[row][col] * (1 / det) for col in range(cols)] for row in range(rows)])
    print()
    main_menu()


main_menu()
