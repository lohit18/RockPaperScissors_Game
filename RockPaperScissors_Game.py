# Start

import random

# Default Values.
options = {'R':'Rock', 'P':'Paper', 'S':'Scissors'}
user_count = 0
computer_count = 0
count = 0

# Input taking from user to loop the given number of times
games = int(input("Enter the number of games you want to play: "))

# Loop Start's here
while count < games:
    print('Enter Any one option [Rock or Paper or Scissors]')
    user_input = input("User's Input: ")[0].upper()

    # The [0] after the input() will assign the first character of input to the variable & converted into upper case.
    # Hence, the user can enter anything, anyway.
    # Like: The user can enter 'Rock' or 'rock' or 'r' or 'R' or 'ro' or any such thing which represents Rock.
    # It will always take input as an R

    flag = 0
    for i in options.keys():
        if user_input == i:             # If the entered input is confined to Rock, Paper or Scissors.
            flag = 1

    if flag != 1:                       # If not, run the loop again.
        print("INVALID INPUT")
        continue
    computer_input = random.choice(list(options.keys()))        # Random Key from the dictionary options i.e. R,P or S.

    print("Computer's Input: ", options[computer_input])
    print("User Input: ", options[user_input])

    if (computer_input == 'R' and user_input == 'S') or (computer_input == 'S' and user_input == 'P') or (computer_input == 'P' and user_input == 'R'):
        computer_count +=1
    elif (user_input == 'R' and computer_input == 'S') or (user_input == 'S' and computer_input == 'P') or (user_input == 'P' and computer_input == 'R'):
        user_count +=1
    else:
        print('=' * 50)
        print('\t\tTIE')

    print('='*50)
    print('\t\tSCORE: ')
    print('computer score:{} \t user score: {}'.format(computer_count, user_count, '\n'))
    count += 1
    # Loop End's

print()
print('=' * 50)
print('\t\t\tFINAL SCORE: ')
print('=' * 50)
print('computer score:{} \t user score: {}'.format(computer_count, user_count, '\n'))
print('=' * 50)
if computer_count > user_count:
    print('\tSORRY! YOU LOST!')
    print('=' * 50)
elif user_count > computer_count:
    print('\tCONGRATULATIONS! YOU WON!')
    print('=' * 50)
else:
    print("\tOOPS! IT'S A TIE!")
    print('=' * 50)

# End!