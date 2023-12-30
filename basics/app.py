print('Hello World')

if 5 > 2: 
 print('Only when condition')

x = str(7)
print(type(x))

y = int(3)
print(type(y))

z = float(3)
print(type(z))

fruits = ['apple', 'banana', 'mango']
a, b, c = fruits

print(a, b, c)

print(a + b + c)


# This is defs
x = 'awesome'

def printFunc(): 
 x = 'simple'
 print('Print the variable ' + x)

printFunc()
print(x)

# Trying global variables
def globalVariable():
 global name
 name = 'Amitav Roy'
 print('Global variable printed ' + name)

globalVariable()
print('Global variable outside ' + name)

