import random

listC = ['Rock', 'Paper', 'Scissor']
choice = ''
print('Welcome to Rock, Paper & Scissor')

while choice is not 'exit':
    choice = input('\nChoose either Rock, Paper or Scissor: ')
    print('Your choice was: ')
    print(choice)
    print('The computer chose:')
    comp = random.choice(listC)
    print(comp)
    choiceH = choice.lower()
    choiceC = comp.lower()
    if choiceH == choiceC:
        print('It is a tie')
    elif choiceH == 'rock' and choiceC == 'scissor' or choiceH == 'paper' and choiceC == 'rock' or choiceH == 'scissor' and choiceC =='paper':
        print('You won!')
    elif choiceC == 'rock' and choiceH == 'scissor' or choiceC == 'paper' and choiceH == 'rock' or choiceC == 'scissor' and choiceH =='paper':
        print('The Computer won!')

