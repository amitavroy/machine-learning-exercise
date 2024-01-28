name = 'Amitav Roy'

if 'Amite' in name:
    print('Present')
else: 
    print('Not present')

print()

if 'amit'.casefold() not in name.casefold():
    print('Not present')
else:
    print('Present')


specialNumber = "9, 123; 4566: 434 56777"
symbols = ""
for char in specialNumber:
    if not char.isnumeric():
        symbols += char

print(symbols)
