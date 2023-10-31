import random

def generate_random_matrix(rows, cols):
    matrix = []
    # _ indicates that we dont use loop variable
    for _ in range(rows):
        row = [random.randint(1, 100) for _ in range(cols)]
        matrix.append(row)
    return matrix

def get_column_sum(matrix, column_index):
    if not matrix or column_index < 0 or column_index >= len(matrix[0]):
        return 0
    column_sum = sum(row[column_index] for row in matrix)
    return column_sum

def get_row_average(matrix, row_index):
    if not matrix or row_index < 0 or row_index >= len(matrix):
        return 0
    row = matrix[row_index]
    row_average = sum(row) / len(row)
    return row_average

random_matrix = generate_random_matrix(3, 4)
print("Random Matrix:")
for row in random_matrix:
    print(row)

column_index = 2 
column_sum = get_column_sum(random_matrix, column_index)
# {} in print are placeholders
print(f"Sum of column {column_index}: {column_sum}")

row_index = 1  
row_average = get_row_average(random_matrix, row_index)
print(f"Average of row {row_index}: {row_average}")