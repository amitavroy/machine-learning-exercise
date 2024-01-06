numbers = [1, 3, 2, 6, 7]

numbers.sort()

new_numbers = sorted(numbers)
print(new_numbers)
print(numbers)

string_to_sort = "The fox jumped over the lazy dog"
check = sorted(string_to_sort, key=str.casefold)
print(check)

# removing numbers in reverse from a list
data = [104, 101, 4, 5, 304, 445, 342, 22, 231, 5, 999, 567, 33, 657, 456]
min_valid = 100
max_valid = 1000

for index in range(len(data) - 1, -1, -1):
    if data[index] < min_valid or data[index] > max_valid:
        del data[index]

print(data)
