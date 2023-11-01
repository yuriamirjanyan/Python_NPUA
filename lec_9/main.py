class Matrix:
    # Constructor
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # Magic method for representation matrix
    def __str__(self):
        matrix_str = ""
        for row in self.data:
            matrix_str += ' '.join(str(val) for val in row) + '\n'
        return matrix_str
    
    # Magic methods for arithmetical operations by matrix
    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must be the same for addition")
        
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must be the same for subtraction")
        
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] - other.data[i][j]
        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix for multiplication")
        
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                result.data[i][j] = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
        return result

# Testing Matrix class
matrix1 = Matrix(2, 2)
matrix1.data = [[1, 2], [3, 4]]

matrix2 = Matrix(2, 2)
matrix2.data = [[5, 6], [7, 8]]

print("Matrix 1:")
print(matrix1)

print("Matrix 2:")
print(matrix2)

# Addition
matrix_sum = matrix1 + matrix2
print("Matrix Sum:")
print(matrix_sum)

# Subtraction
matrix_diff = matrix1 - matrix2
print("Matrix Difference:")
print(matrix_diff)

# Multiplication
matrix3 = Matrix(2, 3)
matrix3.data = [[1, 2, 3], [4, 5, 6]]

matrix4 = Matrix(3, 2)
matrix4.data = [[7, 8], [9, 10], [11, 12]]

matrix_product = matrix3 * matrix4
print("Matrix Product:")
print(matrix_product)