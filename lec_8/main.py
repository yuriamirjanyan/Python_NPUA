import random

class Matrix:
    # constructor
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = []
        for _ in range(n):
            row = []
            for _ in range(m):
                row.append(random.randint(1, 10))
            self.matrix.append(row)

    def print_matrix(self):
        for row in self.matrix:
            print(row)

    def calculate_mean(self):
        total = 0
        for row in self.matrix:
            total += sum(row)
        mean = total / (self.n * self.m)
        return mean

    def calculate_row_sum(self, row_index):
        if 0 <= row_index < self.n:
            return sum(self.matrix[row_index])
        else:
            return None

    def calculate_col_average(self, col_index):
        if 0 <= col_index < self.m:
            col_sum = sum(row[col_index] for row in self.matrix)
            col_average = col_sum / self.n
            return col_average
        else:
            return None

    def print_submatrix(self, col1, col2, row1, row2):
        if 0 <= col1 < col2 <= self.m and 0 <= row1 < row2 <= self.n:
            for i in range(row1, row2):
                print(self.matrix[i][col1:col2])
        else:
            print("Invalid submatrix dimensions")


matrix = Matrix(4, 5)
matrix.print_matrix()
print("Mean of the matrix:", matrix.calculate_mean())
print("Sum of 1st row:", matrix.calculate_row_sum(1))
print("Average of 3th column:", matrix.calculate_col_average(3))
print("Submatrix:")
matrix.print_submatrix(1, 4, 1, 3)