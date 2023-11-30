import random
import time

# Decorator to measure function execution time
def measure_function_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        function_execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {function_execution_time} seconds")
        return result
    return wrapper

# Function to generate random numbers and write to a file
@measure_function_execution_time
def generate_random_numbers(path_of_file):
    with open(path_of_file, 'w') as random_integers_file:
        for _ in range(100):
            random_integers = ' '.join(str(random.randint(1, 80)) for _ in range(20))
            random_integers_file.write(random_integers + '\n')

# Function to convert line to integer array using map
@measure_function_execution_time
def line_to_int_array(line):
    return list(map(int, line.split()))

# Function to filter numbers > 40
@measure_function_execution_time
def filter_numbers(list_of_integers):
    filtered_ints = list(filter(lambda x: x > 40, list_of_integers))
    return filtered_ints

# Function to write filtered data to a file
@measure_function_execution_time
def write_filtered_data(path_of_file, filtered_integers):
    with open(path_of_file, 'w') as filtered_integers_file:
        for line in filtered_integers:
            line_of_integers = ' '.join(map(str, line))
            filtered_integers_file.write(line_of_integers + '\n')

# Function to read a file as a generator using yield
@measure_function_execution_time
def read_file_as_generator(path_of_file):
    with open(path_of_file, 'r') as file:
        for line in file:
            yield line

# Main logic
generate_random_numbers('randomints.txt')  # Generate random numbers and write to a file

with open("randomints.txt", 'r') as random_integers_file:
    data = []
    lines = random_integers_file.readlines()
    for line in lines:
        filtered_integers = filter_numbers(line_to_int_array(line))  # Convert line to int array and filter numbers > 40
        data.append(filtered_integers)  # Append filtered integers to data list

write_filtered_data("filteredints.txt", data)  # Write filtered data to a file

# Read filtered file using a generator and print lines
for line in read_file_as_generator("filteredints.txt"):
    print(line)