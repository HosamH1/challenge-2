print("Please enter 5 numbers:")

# List to store the numbers
numbers = []

# Loop to get 5 numbers from the user
for _ in range(5):
    number = float(input("Enter a number: "))  # Convert input to float
    numbers.append(number)

# Sort the numbers from largest to smallest
numbers.sort(reverse=True)

# Print the sorted list
print("Numbers sorted from largest to smallest:")
for num in numbers:
    print(num)
