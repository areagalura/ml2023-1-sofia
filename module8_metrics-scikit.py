# Ask the user for input N (positive integer)
user_input = input("Please enter a positive integer: ")

# Checking if the N input is a positive integer
try:
    n = int(user_input)
    if n > 0:
        print(f"Thank you entering a positive integer: {n}")
    else:
        print("Sorry, the input is not a positive integer. Try again.")
except ValueError:
    print("Sorry, the input is not a valid integer.")

# Ask the user to provide N (x, y) points (one by one) 
try:
    N = int(input("Please enter the number of points (N): "))
except ValueError:
    print("Sorry, this is an invalid input N. Please enter a valid integer.")
    exit(1)

# Store X and Y values
X_values = []
Y_values = []

# Read all N points one by one 
for i in range(N):
    try:
        # Ask first for the x value (ground truth), X is either 0 or 1
        x = int(input(f"Enter the x value for point {i + 1} (0 or 1): "))
        if x not in [0, 1]:
            print("You have an invalid input N. Please enter 0 or 1 for x to continue.")
            exit(1)

        # Ask then for the y value (predicted class), Y is either 0 or 1
        y = int(input(f"Enter the y value for point {i + 1} (0 or 1): "))
        if y not in [0, 1]:
            print("You have an invalid input N. Please enter 0 or 1 for y to continue.")
            exit(1)

        # Append to the X and Y lists
        X_values.append(x)
        Y_values.append(y)
    except ValueError:
        print("You have an invalid input N. Please enter valid integers for x and y to continue.")
        exit(1)

# Print the X and Y data
print("Collected X and Y data:")
for i in range(N):
    print(f"Point {i + 1}: (X = {X_values[i]}, Y = {Y_values[i]})")

# Calculate Precision and Recall based on the inputs
def calculate_precision_recall(X_values, Y_values):
    true_positives = sum(1 for x, y in zip(X_values, Y_values) if x == 1 and y == 1)
    false_positives = sum(1 for x, y in zip(X_values, Y_values) if x == 0 and y == 1)
    false_negatives = sum(1 for x, y in zip(X_values, Y_values) if x == 1 and y == 0)

    if true_positives + false_positives == 0:
        precision = 0
    else:
        precision = true_positives / (true_positives + false_positives)

    if true_positives + false_negatives == 0:
        recall = 0
    else:
        recall = true_positives / (true_positives + false_negatives)

    return precision, recall

try:
    # Ask the user for input N (positive integer)
    N = int(input("Enter the number of points (N, positive integer): "))

    if N <= 0:
        print("N must be a positive integer.")
    else:
        X_values = []
        Y_values = []

        # Read N (x, y) points one by one
        for i in range(N):
            x = int(input(f"Enter the x value for point {i + 1} (0 or 1): "))
            if x not in [0, 1]:
                print("Invalid input for x. Please enter 0 or 1.")
                exit(1)

            y = int(input(f"Enter the y value for point {i + 1} (0 or 1): "))
            if y not in [0, 1]:
                print("Invalid input for y. Please enter 0 or 1.")
                exit(1)

            X_values.append(x)
            Y_values.append(y)

        # Calculate Precision and Recall
        precision, recall = calculate_precision_recall(X_values, Y_values)

        # Output the results
        print(f"Precision: {precision:.2f}")
        print(f"Recall: {recall:.2f}")

except ValueError:
    print("Sorry, this is an invalid input N. Please enter a valid integer.")
