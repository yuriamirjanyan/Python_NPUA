def multiply_matrix_by_vector(matrix, vector):
    matrix_rows = len(matrix)
    matrix_cols = len(matrix[0]) if matrix_rows > 0 else 0
    vector_length = len(vector)

    # matrici ev vektori chapery petqe linen havasar
    if matrix_cols == 0:
        raise ValueError('Matrix must have at least one column.')
    if matrix_rows == 0:
        raise ValueError('Matrix must have at least one row.')
    if any(len(row) != matrix_cols for row in matrix):
        raise ValueError('All rows in the matrix must have the same number of columns.')
    if vector_length != matrix_cols:
        raise ValueError('The length of the vector must be equal to the number of columns in the matrix.')

    result = []
    for row in matrix:
        sum = 0
        for a, b in zip(row, vector):
            sum += a * b
        result.append(sum)
    return result

# objecty file-um grelu funkcia
def write_to_file(filename, data):
    with open(filename, 'w') as file:
        for element in data:
            file.write(str(element) + '\n')


# test multiply_matrix_by_vector function
matrix = [[2, 3, 1], [7, 5, 10], [9, 6, 8], [4, -9, 12]]
vector = [2, 4, 3]

# Output the result to a file
try:
    result = multiply_matrix_by_vector(matrix, vector)
    filename = 'matrix_vector_multiplication.txt'
    write_to_file(filename, result)
    print(f'Result successfully written to {filename}')
except ValueError as e:
    print('Error happened:', str(e))