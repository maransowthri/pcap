from random import randint

print('--- Rock Paper Scissors Game ---')
rounds = input('How many rounds would you like to play? ')

while not rounds.isdigit():
    print('Please enter valid input')
    rounds = input('How many rounds would you like to play?')

rounds = int(rounds)
player_won_count = 0
robot_won_count = 0

while rounds > 0:
    valid_choices = ['r', 'p', 's']
    player_choice = input('Rock, paper or scissors [r/p/s]? ')

    while player_choice not in valid_choices:
        print('Please enter valid choice')
        player_choice = input('Rock, paper or scissors [r/p/s]? ')

    robot_choice = valid_choices[randint(0, 2)]

    print(f'You: {player_choice} | Robot: {robot_choice}')
    
    if robot_choice == player_choice:
        print('This round is a tie')
    elif robot_choice == 's' and player_choice == 'p':
        robot_won_count += 1
        print('You lost this round!')
    elif robot_choice == 'p' and player_choice == 's':
        player_won_count += 1
        print('You won this round!')
    elif robot_choice == 'p' and player_choice == 'r':
        robot_won_count += 1
        print('You lost this round!')
    elif robot_choice == 'r' and player_choice == 'p':
        player_won_count += 1
        print('You won this round!')
    elif robot_choice == 'r' and player_choice == 's':
        robot_won_count += 1
        print('You lost this round!')
    elif robot_choice == 's' and player_choice == 'r':
        player_won_count += 1
        print('You won this round!')

    print()
    rounds -= 1

print(f'[Game Summary] Your Points: {player_won_count} | Robot Points: {robot_won_count}')

if player_won_count > robot_won_count:
    print('You won')
elif player_won_count == robot_won_count:
    print('It was a tie')
else:
    print('Robot won')
