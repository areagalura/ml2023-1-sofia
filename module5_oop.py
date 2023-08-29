# Function to get a positive integer input from the user
def get_positive_integer():
    while True:
        try:
            n = int(input("Provide a positive integer (N): "))
            if n > 0:
                return n
            else:
                print("Please provide a positive integer or any number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

# Function to get the positive intger and read it
if __name__ == "__main__":
    N = get_positive_integer()
    print(f"You inputted this postive integer: {N}")



# Function to ask user to provide N numbers one by one  
def get_positive_integer():
    while True:
        try:
            n = int(input("Provide a positive integer (N): "))
            if n > 0:
                return n
            else:
                print("Please provide a positive integer or any number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


# Function to read and store N numbers
def read_Nnumbers(N):
    numbers = []
    for i in range(N):
        while True:
            try:
                num = int(input(f"Provide number {i+1}/{N}: "))
                numbers.append(num)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    return Nnumbers

# Function to read the integer one by one
if __name__ == "__main__":
    N = get_positive_integer("Enter the number of integers you want to input (N): ")
    numbers = read_numbers(N)
    
    print("You entered the following numbers:")
    for i, num in enumerate(numbers):
        print(f"Number {i+1}: {num}")


# Function to find the index of X in the list
def find_index_of_X(numbers, X):
    for i, num in enumerate(numbers):
        if num == X:
            return i + 1  # Add 1 to make the index 1-based
    return -1

# Function to check there is no such X among N read numbers, or the index (from 1 to N) of this X if the user inputted it before
if __name__ == "__main__":
    N = get_positive_integer("Enter the number of integers you want to input (N): ")
    numbers = read_numbers(N)
    
    X = int(input("Enter an integer (X): "))
    index = find_index_of_X(numbers, X)
    
    if index != -1:
        print(f"{X} was found at position {index} among the entered numbers.")
    else:
        print(f"{X} was not found among the entered numbers.")
