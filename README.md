# Challenge 2: Sort and Print Numbers in Descending Order

Welcome to Challenge 2! This challenge is designed to test your ability to manipulate lists in Python, specifically focusing on sorting elements. You are provided with a starter code that prompts the user to enter 5 numbers, stores them in a list, and then prints them out. Your task is to adjust the code to sort these numbers from largest to smallest before printing.

## Getting Started

To get started with this challenge, you'll need a Python environment set up on your machine. If you don't have Python installed, please follow the [official Python installation guide](https://www.python.org/downloads/).

### Prerequisites

- Python 3.x installed on your local machine.

### Setup

1. Create a new Python file on your local machine and name it `challenge2.py`.
2. Copy the starter code provided below into your `challenge2.py` file.

```python
print("Please enter 5 numbers:")

# List to store the numbers
numbers = []

# Loop to get 5 numbers from the user
for _ in range(5):
    number = float(input("Enter a number: "))  # Convert input to float
    numbers.append(number)

# TODO: Sort the numbers from largest to smallest

# Print the sorted list
print("Numbers sorted from largest to smallest:")
for num in numbers:
    print(num)






