class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator
        self.simplify() # krjatel kotoraky

    def simplify(self):
        common = self.gcd(self.numerator, self.denominator)
        self.numerator //= common
        self.denominator //= common

    # gcd()-n gtnum e amenamec yndhanur bajanarary
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    # tpum e kotoraky
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)
        
# Test Fraction class
f1 = Fraction(1, 2)
f2 = Fraction(3, 4)

print("Fraction 1:", f1)
print("Fraction 2:", f2)

result_add = f1 + f2
result_sub = f1 - f2
result_mul = f1 * f2
result_div = f1 / f2

print("Addition:", result_add)
print("Subtraction:", result_sub)
print("Multiplication:", result_mul)
print("Division:", result_div)
