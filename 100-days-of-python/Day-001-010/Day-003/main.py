alphabets = 'abcdefghijklmnopqrstuvwxyz'
print(alphabets[16:13:-1]) # just get qpo - run reverse
print(alphabets[4::-1]) # edcba get in reverse
print(alphabets[15:10:-1])
print(alphabets[11:16])
print(alphabets[25:-4:-1])
print(alphabets[-3:]) # last 3 chars

# Multiple print of word
print("Amitav " * 5)

# Printing with alignment
for i in range(1, 10):
    print("No. {0} sqaured {1:3} is {2:4}".format(i, i ** 2, i ** 3))

# Printing with alignment and left align
print()
for i in range(1, 10):
    print("No. {0} sqaured {1:<3} is {2:4}".format(i, i ** 2, i ** 3))

days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])
