# Function to classify numbers as even or odd
def classify_numbers(numbers):
    even_numbers = []
    odd_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    return even_numbers, odd_numbers

# input numbers
input_nums = input("Enter a list of numbers seperated by spaces: ")

# convert splited strings to int and storage in a list
nums_list = [int(num) for num in input_nums.split()]

# call classify_numbers function
even_nums, odd_nums = classify_numbers(nums_list)

# Print the results
print("Even numbers:", even_nums)
print("Odd numbers:", odd_nums)
