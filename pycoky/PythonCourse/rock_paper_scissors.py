import random

computer_choice = random.choice(['scissors', 'rock', 'paper'])
user_choice = input('Do you want - rock, paper, or scissors?\n')
if computer_choice == user_choice: 
    print (computer_choice  + "Tie" +  "Everybody Wins!")
elif user_choice == 'rock' and computer_choice == 'scissors':
    print(computer_choice + "-" + 'You are the Winner!')
elif user_choice == 'paper' and computer_choice == 'rock': 
    print(computer_choice + "-" + "You are the Winner!")
elif user_choice == 'scissors' and computer_choice == 'paper':
    print(computer_choice + "-" + "You are the Winner!")
else: 
    print(computer_choice + "-" + "So Sorry! The Computer Wins!")
