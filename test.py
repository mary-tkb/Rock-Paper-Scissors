import random

choices = ['r', 'p', 's']
def start(input):
  if input == 'r':
    return 'Rock'
  elif input == 's':
    return 'Scissors'
  elif input == 'p':
    return 'Paper'
  else:
    return 'Try again with an appropriate letter'

print('Rock: r, Paper: p, Scissors: s - Shoot!')
print('[Q] = Quit\n')
c = 1
ucw = 0
ccw = 0
while True:
   print(f'Game {str(c)}:')
   print('Please choose a letter:')
   uc = input()
   if uc == 'Q':
      print('Thanks for playing !')
      print(f'yor score is: {ucw} and computer score is {ccw}')
      break;
  
   ind = random.randint(0, 2)
   cc = choices[ind] 
 
   print(f'You chose: {start(uc)} and the computer chose:{start(cc)}')
   
   if uc == 'r' and cc == 's':
      print('You win, Rock beats Scissors')
      ucw = ucw+1
   elif uc == 'p' and cc== 'r':
      print('You win, Paper beats Rock')
      ucw = ucw+1
   elif uc=='s' and cc=='p':
      print('You win, Scissors beats Paper')
      ucw = ucw+1
   elif uc == 'r' and cc== 'p':
      print('Computer wins, Paper beats Rock')
      ccw = ccw+1
   elif uc == 'p' and cc == 's':
      print('Computer wins, Scissors beats Paper')
      ccw = ccw+1
   elif uc=='s' and cc=='r':
      print('Computer wins, Rock beats Scissors')
      ccw = ccw+1
   elif uc == cc:
      print('It is a tie !')
   else:
      print('Please enter your choice or [Q]')
      
   c = c + 1
   print(f'yor score is: {ucw} and computer score is {ccw}')
   print('\n')