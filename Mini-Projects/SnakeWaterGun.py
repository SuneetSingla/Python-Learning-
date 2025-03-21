# 1 for snake
# -1 for water
# 0 for gun
import random

def computer_choice () :
    choices = ['snake', 'water', 'gun']
    comp =  random.choice(choices)
    print("Computer chose : ", comp)

def user_choice ():
    print("Enter your choice : ")
    userinput = int(input("\n1 for snake\n-1 for water\n0 for gun\n"))
    choicesdict = {1 : 'snake', -1 : 'water', 0 : 'gun'}
    user = choicesdict[userinput]
    print("You chose : ", user)
    

def game():
    computer = computer_choice()
    user = user_choice()
    if computer == user :
        return "It's a tie"
    elif computer == 'snake' and user == 'water' :
        return "Computer wins"
    elif computer == 'water' and user == 'gun' :
        return "Computer wins"
    elif computer == 'gun' and user == 'snake' :
        return "Computer wins"
    else :
        return "User wins"
    
print(game())



