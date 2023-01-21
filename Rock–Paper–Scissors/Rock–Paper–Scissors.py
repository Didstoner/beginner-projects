import random

score_player = 0
score_computer = 0

rock = 'rock'
paper = 'paper'
scissors = 'scissors'
player_move = input('Chose [r]ock, [p]aper, [s]cissors or [e]nd: ')
while player_move != 'e':
    if player_move == 'r':
        player_move = rock
    elif player_move == 'p':
        player_move = paper
    elif player_move == 's':
        player_move = scissors
    else:
        print('Invalit input.Try again...')
        player_move = input('Chose [r]ock, [p]aper, [s]cissors or [e]nd: ')
        continue

    computer_random_number = random.randint(1, 3)
    computer_move = ''
    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    elif computer_random_number == 3:
        computer_move = scissors
    print(f"The computer chose {computer_move}.")
    if (player_move == 'rock' and computer_move == 'scissors') or (
            player_move == 'paper' and computer_move == 'rock') or (
            player_move == 'scissors' and computer_move == 'paper'):
        print('You win')
        score_player += 1
    elif player_move == computer_move:
        print('Draw!')
    else:
        print('Computer win!')
        score_computer += 1

    player_move = input('Chose [r]ock, [p]aper, [s]cissors or [e]nd: ')
if score_player > score_computer:
    print(f"You are winner with score:{score_player}")
elif score_player == score_computer:
    print('you are equal!')
else:
    print(f"Computer is winner with score:{score_computer}")
