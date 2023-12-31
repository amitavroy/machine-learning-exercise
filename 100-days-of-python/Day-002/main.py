# Understanding variables

name = 'Amitav Roy'
countryCode = 91
tech = ['php', 'js', 'react', 'vue']
skills = [{'name': 'php', 'level': 5}]

print(type(name))
print(type(countryCode))
print(type(tech))
print(type(skills))

# Data type related code
age = 30
pi = 3.14
print(pi + 1)

for i in range(1, 22 // 7):
    print(i)

# Understanding substring
# Forward movement
name = 'Amitav Roy'

print(name[7])
print()

# Backward movement
print(name[-3])

# Printing multiplication table using concat
number = 7
result = ""
for i in range(1, 11):
    result = result + "\n" + f'{number} X {i} = {number * i}'

print(result)

# other ways of concatination
number2 = 9
print('I have a number and the value is {0} and another {1}'.format(number, number2))

# Looking at slicing
name = 'Amitav Roy'
print(name[0:4]) # starting 4
print(name[:4]) # starting 4 one more version
print(name[7:10]) # 7 to 10 to get Roy
print(name[-3:]);

# Reversing string = ::-1
alphabets = 'abcdefghijklmnopqrstuvwxyz'
print(alphabets[25::-1]) # 0 vs not specifying has an advantage
print(alphabets[::-1]) # using same for the start
