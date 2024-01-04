high = 100
low = 1
guesses = 1

input('Press ENTER to start')

while True:
    print("\tGuessing in the range of {} to {} with guess {}".format(low, high, guesses))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower?"
                     "Enter h or l, or c if my guess was correct".format(guess)).casefold()

    if high_low == 'h':
        low = guess + 1
    elif high_low == 'l':
        high = guess - 1
    elif high_low == 'c':
        print('I got it in {} guesses!'.format(guesses))
        break
    else:
        print('Need to enter h, l or c')
    guesses = guesses + 1

# assignment code
number = 5
multiplier = 8
answer = 0
 
# add your loop after this comment
for i in range(multiplier):
    answer += number
 
print(answer)
