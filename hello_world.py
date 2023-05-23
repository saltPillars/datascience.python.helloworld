# String Exercises

# 2-3 Personal Message
wrestler = "Rhea Ripley"
message = f"My favorite wrestler is {wrestler}"
print(message)

# 2-4 Name Cases
name = 'cHad gAble'
print(name)
print(name.lower())
print(name.upper())
print(name.title())

# 2-5 Famous Quote
quote = 'The Rock once said "Ahh shut your mouth, you thong-wearing fatty!"'
print(quote)

# 2-6 Famous Quote 2
wrestler = "the rock"
quote = "Know your role and shut your mouth"
message = f'{wrestler.title()} once said, "{quote}".'
print(message)

# 2-7 Stripping Names
wrestler = "  \t\t\t\t\tSonya Deville\n\n\n\n   "
print(f"|{wrestler}|")
print(f"|{wrestler.lstrip()}|")
print(f"|{wrestler.rstrip()}|")
print(f"|{wrestler.strip()}|")