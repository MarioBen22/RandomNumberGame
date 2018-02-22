# Mario Benavides
# this game randomly chooses a number between 1 and 100
# you guess until you get it

import random
randomnumber = random.randint(1,100)
print('Guess a number between 1 and 100')

found = False


while not found:
	userguess = int(input('What is your guess: '))
	if userguess == randomnumber:
		print('You got it!')
		found = True
	elif userguess > randomnumber:
		print('Try again, guess lower')
	else:
		print('Try again, guess higher')
		
