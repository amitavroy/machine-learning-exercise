# Basic type of printing

# The basic thing to start learning
print('Hello World!')

# Multiple params
print('This', 'takes', 'dynamic', 'number')

# Concatenate strings
print('My name is ' + 'Amitav Roy')

# User input work
# name = input("Enter your name ")
# print("Hello " + name)

# Trying our escapre characters
# Spaces are considered after the \n
print()
print("This is line 1\n and this is new line")
print("This is a \t space")
print('Delimiters does work he\'s working and it\'s working')
print("Delimiters does work he's working and it's working")

# Triple quotes is interesting
print("""Any kind of quote's can come "Why I am here"?""")

print()
stringToPrint = """The here doc version of Python is quite neat.
I can just have three " quotes i.e. and
then span across multiple lines."""
print(stringToPrint)

print()
consoleStyle = """If you want console type formatting\
Then, just adding a back slash works \
as if I am writing a console code.
Or something very common with Dockerfiles \
as well.
"""
print(consoleStyle)

# Raw string
print(r"C:\Users\timberlake\notes.txt")
