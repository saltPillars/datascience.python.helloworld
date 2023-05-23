# Whitespace Fun

# \t adds a tab
print("\tPython")

# \n adds a new line
print("Languages:\nPython\nC\nJavaScript")

# can use multiple in one string
print("Languages:\n\tPython\n\tC\n\tJavascript")

# Whitespace in a string is considered significant unless otherwise told
# Whitespace can be removed to sanitize data

# .rstrip() removes whitespace from the end of a string
favorite_language = 'python '
print(f"{favorite_language}|")
print(f"{favorite_language.rstrip()}|")

# .rstrip() only removes the whitespace on the fly temporarily
print(f"{favorite_language}|")
favorite_language = favorite_language.rstrip()
print(f"{favorite_language}|")

# .lstrip() removes whitespace from the beginning of a string
favorite_language = '  python'
print(f"{favorite_language}")
print(f"{favorite_language.lstrip()}")

# .strip() removes whitespace from the beginning and end of a stringfavorite_language = '  python'
favorite_language = '   python    '
print(f"|{favorite_language}|")
print(f"|{favorite_language.strip()}|")