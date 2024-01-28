import random

# loop backwards
for i in range(10, 0, -2):
    print(i)

print()

# normal loop
for i in range(10, 0, -1):
    print(i)

# iterate through list
print()
movies = ['Avengers', 'Captain America', 'Star Wars', 'Titanic', 'Transporter']

for movie in movies:
    if movie is not 'Titanic':
        print(movie)

# iterate and skip on condition
print()
for movie in movies:
    if movie == 'Titanic':
        continue
    print(movie)

# looking for index
print()
tofind = 'Titanic'
for index in range(len(movies)):
    if movies[index] == tofind:
        print(index)
        break

# The simpler version
if 'Titanic' in movies:
    print('Yes')

# While loop
print()
i = 0
while i < 10:
    print(i)
    i+=1

print()
print(random.randint(1, 10))
