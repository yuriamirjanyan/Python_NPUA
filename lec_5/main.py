# function to calculate summary numbers
def sum_of_elements(numbers, exclude_negative = False):
    if exclude_negative:
        filtered_numbers = [num for num in numbers if num >= 0]
    else:
        filtered_numbers = numbers
    # sum() calculates the summary of all the elements
    return sum(filtered_numbers)


# input numbers
input_nums = input("Enter a list of numbers seperated by spaces: ")

# convert splited strings to int and storage in a list
numbers = [int(num) for num in input_nums.split()]

answer = input("Do you want to exclude negative numbers? (yes or no): ")

# check answer
if answer.lower() == "yes":
    exclude_negative = True
else:
    exclude_negative = False

result = sum_of_elements(numbers, exclude_negative)

if exclude_negative:
    print("Sum of positive numbers: ", result)
else:
    print("Sum of all numbers (including negative): ", result)