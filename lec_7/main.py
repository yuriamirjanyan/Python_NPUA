def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print("File content:\n", content)
    except FileNotFoundError:
        print(f"The file '{file_name}' doesn't exist. Please enter a valid filename.")
        return False
    return True

def write_file(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
    except FileNotFoundError:
        print(f"Could not create the file '{file_name}'. Please enter a valid filename.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
    else:
        print("Writing to the file was successful.")
    finally:
        print("File has been closed.")

while True:
    file_name = input("Enter the name of the text file you want to open (or 'q' to quit): ")
    
    if file_name.lower() == 'q':
        break
    
    try:
        if not read_file(file_name):
            continue
    except ValueError:
        print("Invalid filename. Please enter a valid filename.")
        continue

    option = input("Do you want to write to this file? (y/n): ").lower()
    
    if option == 'y':
        new_content = input("Enter the content you want to write to the file: ")
        try:
            write_file(file_name, new_content)
        except ValueError:
            print("Invalid filename. Please enter a valid filename.")