# Rock paper scissors text game implementation
# Written in python 3.6
# Written by Doug Purcell
# The player can play an unlimited number of times,and
# then the score will be tracked at the end.
#
#####################################################

import random

you = ''
options = ['R', 'P', 'S']

def run(games = 1):
    """ game loop """
    print('Welcome to Rock Paper Scissors in Python:')
    print('PLAY by typing one of the following below: \n R -> Rock\n P -> '
          'Paper\n ' 'S -> Scissors')

    x, y, z = 0, 0, 0
    score = {'you': x, 'computer': y, 'draw': z}

    while True:
        print('Round # {}. Do you choose \'R\', \'P\', or \'S\'?'.
            format(games))
        games += 1
        computer = random.choice(options)
        you = input().upper()
        if you == 'X':
            print("Time to exit...")
            print('your score = {} computer score = {} draws = {}'.
                      format(score['you'],score['computer'],score['draw']))
            exit(0)
        elif not(you == 'R' or you == 'S' or you == 'P'):
            print("\n{} is invalid input!".format(you))
            print('your score = {} computer score = {} draws = {}'.
                  format(score['you'],score['computer'],score['draw']))
            print("EXITING...")
            exit(0)
        else:
            if you == 'R' and computer == 'R':
                score['draw'] += 1
                print('Computer chooses {}'.format(computer))
                print('DRAW')
            elif you == 'P' and computer == 'P':
                score['draw'] += 1
                print('Computer chooses {}'.format(computer))
                print('DRAW')
            elif you == 'S' and computer == 'S':
                score['draw'] += 1
                print('Computer chooses {}'.format(computer))
                print('DRAW')
            elif you == 'R' and computer == 'P':
                score['computer'] += 1
                print('Computer chooses {}'.format(computer))
                print('Computer wins! Paper covers Rock!')
            elif you == 'R' and computer == 'S':
                score['you'] += 1
                print('Computer chooses {}'.format(computer))
                print('You win! Rock smashes Scissors!')
            elif you == 'P' and computer == 'R':
                score['you'] += 1
                print('Computer chooses {}'.format(computer))
                print('You Win! BOOM. Paper covers Rock!')
            elif you == 'S' and computer == 'R':
                 score['computer'] += 1
                 print('Computer chooses {}'.format(computer))
                 print('Computer wins! Rock smashes Scissors!')
            elif you == 'P'and computer == 'S':
                score['computer'] += 1
                print('Computer chooses {}'.format(computer))
                print('Computer wins! Ouch. Scissors cut Paper!')
            elif you == 'S' and computer == 'P':
                score['you'] += 1
                print('Computer chooses {}'.format(computer))
                print('You win! Scissor slices Paper!')

game_rules = ('\n'
              'Rock paper scissors game rules:\n\n'
              'R = Rock, S = Scissors, P = Paper\n'
              'R vs R = tie\nP vs P = tie\nS vs S = tie\n'
              'R vs P = P wins\n'
              'S vs P = S wins\n'
              'R vs S = R wins\n'
              '________________\n')

print(game_rules)
print('Want to play? Hit \'Y\' to play or \'N\' to exit\n')
start = input().upper()

if start == 'Y':
    run()
elif start == 'N':
    print('You''\'ve entered {} so exiting...'.format(start))
else:
    print('You''\'ve entered {} which is invalid so exiting..'
          '.'.format(start))


