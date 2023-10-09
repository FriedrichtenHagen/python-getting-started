# guess the number

import random

print('I am thinking of a number between 1 and 20.')
print('Take a guess!')

answer = random.randint(1,20)

for i in range(6):
    guess = int(input())
    if guess == answer:
        print(f'Correct answer! It took you {i} tries')
        break
    elif guess < answer:
        print('lower than answer')
    elif guess > answer:
        print('higher than answer')
if guess != answer:
    print(f'correct answer: {answer}')