name = "ada lovelace"

# prints literal string
print(name)

# prints Ada Lovelace
print(name.title())

# prints uppercase
print(name.upper())

# f-strings are used for formatting
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print (f"Hello, {full_name.title()}!")

# f-strings can be stored in variables
full_name = f"{first_name} {last_name}"
message = f"Welcome, {full_name.title()}"
print(message)

# Use format() if using Python 3.5 or earlier instead of f-strings
full_name = "{} {}".format(first_name, last_name)
print(full_name)