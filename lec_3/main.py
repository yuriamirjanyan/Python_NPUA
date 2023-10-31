# Basic operations functions
def Add(number1, number2):
    return number1 + number2;

def Sub(number1, number2):
    return number1 - number2;

def Mul(number1, number2):
     return number1 * number2;

def Div(number1, number2):
     if number2 == 0:
       return "Division by zero is not allowed";
     else:
       return number1 / number2;

expression = input("Expression: ")

# Convertiion between string to a float ignores whitespaces
if "+" in expression:
    number = expression.split("+")
    result = Add(float(number[0]), float(number[1]))
elif "-" in expression:
    number = expression.split("-")
    result = Sub(float(number[0]), float(number[1]))
elif "*" in expression:
    number = expression.split("*")
    result = Mul(float(number[0]), float(number[1]))
elif "/" in expression:
    number = expression.split("/")
    result = Div(float(number[0]), float(number[1]))
else:
    result = "Inavlid expression"

print("Result: ", result)

