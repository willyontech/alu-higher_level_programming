import random

# The following line generates a random signed integer
number = random.randint(-10, 10)

# Print the number
print(number, end=' ')

# Check if the number is positive, zero, or negative
if number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")
