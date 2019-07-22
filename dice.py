#Dice
import random

outcomes = [1,2,3,4,5,6]
decisions = [1,2]

decision = input('Do you wanna roll 1 dice or 2 dice?: ')
decision = int(decision)

def execute():
    outcome = outcomes[random.randint(0,5)]
    print(f'The dice rolled a {outcome}')

def execute_alternative():
    outcome1 = outcomes[random.randint(0,5)]
    outcome2 = outcomes[random.randint(0,5)]
    print(f'The 1st dice rolled a {outcome1}')
    print(f'The 2nd dice rolled a {outcome2}')

    sum = outcome1 + outcome2
    print(f'The total roll is {sum} ')

if(decision == decisions[0]):
    execute()
else:
    execute_alternative()

input('Press ENTER to exit')
