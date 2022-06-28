import random


def get_user_choice():
    user_choices = input('Welcome to the game!Please select rock, paper or scissors:')
    
    return user_choices


def get_computer_choice():
    choice= random.choice(['rock', 'paper', 'scissors'])
    print('Computer chose:' + choice)
    return choice
    
    
def get_winner(user_choice , comp_choice):
    if user_choice == comp_choice:
       print('Tie Darling!')
       
    if user_choice == 'rock':
        if comp_choice == 'paper':
            print('Sorry!Computer Wins!')
        elif comp_choice == 'scissors':
            print('Yeees!You Win Darling!')
            
    elif user_choice == 'paper':
        if comp_choice == 'rock':
            print('Yeees!You Win Darling!')
        elif comp_choice == 'scissors':
            print('Sorry!Computer Wins!')
            
    elif user_choice == 'scissors':
        if comp_choice == 'rock':
            print('Sorry!Computer Wins!')
        elif comp_choice == 'paper':
            print('Yeees!You Win Darling!')
            


user_choice = get_user_choice()
comp_choice = get_computer_choice()

get_winner(user_choice,comp_choice)

        
        
    