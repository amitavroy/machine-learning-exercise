movies = ['Avengers', 'Captain America', 'Star Wars', 'Titanic', 'Transporter']

print(movies[0:3])
print(movies[-1])

movies += ['Cars'] # mutating the list
movies.append('Kungfu Panda')
print(movies)

parts = ['Monitor', 'CPU', 'HDD', 'Mouse', 'Keyboard']
print('Choose the parts that you want to add')
for i, part in enumerate(parts):
    print('{0} for {1}'.format(i, part))

choices = []
while True:
    print('Enter the number or x to exit')
    choice = input()
    if choice == 'x':
        break
    choices.append(parts[int(choice)])

print(choices)
