from random import randint

# Create a list of play options
t = ['Rock', 'Paper', 'Scissors']

# assign a random play to the computer
computer = t[randint(0, 2)]

# Set player to False
player =False

while player == False:
# Set player to True
    player = input('\nEnter "Q" to quit \nRock, Paper, Scissors? ').title()
    if player == computer:
        print('Tie!')
    elif player == 'Rock':
        if computer == 'Scissors':
            print('You win!', player, 'smashes', computer)
        else:
            print('You lose!', computer, 'covers', player)
    elif player == 'Paper':
        if computer == 'Rock':
            print('You win!', player, 'covers', computer)
        else:
            print('You lose!', computer, 'cuts', player)
    elif player == 'Scissors':
        if computer == 'Paper':
            print('You win!', player, 'cuts', computer)
        else:
            print('You lose!', computer, 'smashes', player)
    elif player == 'Q':
        break
    else:
        print("That's not a valid play. Check your spelling!")
 
    # Player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0, 2)]
    if player == 'Q':
        break