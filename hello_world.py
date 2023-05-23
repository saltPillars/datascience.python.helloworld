# Numbers

# add (+)
print(2 + 3)

# subtract (-)
print(3 - 2)

# multiply (*)
print(2 * 3)

# divide (/)
print(3 / 2)

# exponents (**)
print(3 ** 2)

# Order of operations is honored
print(2 + 3 * 4)
print((2 + 3) * 4)

# Decimals are floats. Integers are whole numbers.
# Python should handle most floats without intervention as you would expect
print(0.1 + 0.1)
print(2 * 0.2)

# Sometimes, however, you can get arbitrary decimal points but it happens in most languages
# We'll learn to deal with it later
print(0.2 + 0.1)
print(3 * 0.1 )

# When dividing any two numbers you'll get a float even if they're integers
print(4 / 2)

# When mixing integers and floats you'll get a float
print(1 + 2.0)
print(2 * 3.0)

# When writing long numbers you can group digits with underscores so the number is more readable
universe_age = 14_000_000_000
print(universe_age)

# Python will disregard the underscores when storing the number
number_one = 1000
number_two = 10_00
print(number_one)
print(number_two)

# Multiple Assignments
# You can assign values to more than one variable in one line
x, y, z = 0, 1, 2
print(f"x: {x}\ny: {y}\nz: {z}")

# Constants
# Constants are variables that stay the same
# Names are always capitalized
MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS)

