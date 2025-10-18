"""
Learning Random
Challenge: Fortune Cookie Project
"""

import random

random.randint(1, 10)

print(random.randint(1, 6))

eight_ball = random.randint(1, 3)

if eight_ball == 1:
    print("yes")
elif eight_ball == 2:
    print("no")
else:
    print("maybe")

#Making a Fortune Cookie with random lucky numbers

lucky_number = random.randint(1, 99)

fortune = random.randint(1, 5)

if fortune == 1:
    print(f"You're going to have a great day! Your lucky number is: {lucky_number}")
elif fortune == 2:
    print(f"Watch your back. Someone close to you is not a friend. Your lucky number is: {lucky_number}")
elif fortune == 3:
    print(f"Today will be pretty average. That's good. Your lucky number is: {lucky_number}")
elif fortune == 4:
    print(f"Jesse didn't wash his hands last time he peed. Your lucky number is: {lucky_number}")
else: 
    print(f"You will either find $5 or lose $5. I hope for you. Your lucky number is: {lucky_number}")

#Alternative way to do the fortune cookie

fortune_text = ''

if fortune == 1:
    fortune_text = 'You\'re going to have a great day!'
elif fortune == 2:
    fortune_text = 'Watch your back. Someone close to you is not a friend.'
elif fortune == 3:
    fortune_text = 'Today will be pretty average. That\'s good.'
elif fortune == 4:
    fortune_text = 'Jesse didn\'t wash his hands last time he peed.'
else:
    fortune_text = 'You will either find $5 or lose $5. I hope for you.'

print(f"{fortune_text} Your lucky number is: {lucky_number}")