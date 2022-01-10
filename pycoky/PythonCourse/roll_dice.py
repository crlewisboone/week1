import random
roll = random.randint(1,6)
guess = int(input('Guess the dice roll:\n'))
print("The Computer Rolled a " + str(roll))
if guess == roll:
    print("Correct! The Computer Rolled a " + str(roll))
else:
    print("Oh No! I'm Sorry! The Computer rolled a " + str(roll))
    