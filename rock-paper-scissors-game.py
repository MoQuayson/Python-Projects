import random

#user function
def User(choice):
    if(choice == 'R' or choice == 'r'):
        print('User: Rock')
        return 'Rock'
    
    elif(choice == 'P' or choice == 'p'):
        userValue =2
        print('User: Paper')
        return 'Paper'
    
    elif(choice == 'S' or choice == 's'):
        print('User: Scissors')
        return 'Scissors'

    elif(choice == 'Q' or choice == 'Q'):
        quit()
    
    else:
        print('User: N/A')
        return 'N/A'
        
    

        
    

#computer function
def CPUAI():
    cpuValue =  random.randint(1, 3)
    if(cpuValue == 1):
        print('AI: Rock')
        return 'Rock'
    
    elif(cpuValue == 2):
        print('AI: Paper')
        return 'Paper'
    
    else:
        print('AI: Scissors')
        return 'Scissors'

print('WELCOME TO ROCK PAPER SCISSORS GAME')
user_choice = input('CHOOSE ROCK(R),PAPER(P),SCISSORS(S) OR (Q) TO QUIT: ')[0] #user choice

#while loop until user's choice is Q i.e for QUIT
while(user_choice != 'Q' or user_choice != 'q'):
    #Retrive both values for user and the CPU
    userValue = User(user_choice)
    cpuValue = CPUAI()

    #Results
    #Paper beats rock
    if(userValue == 'Rock' and cpuValue == 'Paper'):
        print('CPU Wins!!')
    
    elif(cpuValue == 'Rock' and userValue == 'Paper'):
        print('User Wins!!')

    #Rock beats Scissors
    elif(userValue == 'Rock' and cpuValue == 'Scissors'):
        print('User Wins!!')
    
    elif(cpuValue == 'Rock' and userValue == 'Scissors'):
        print('CPU Wins!!')
    
    #Scissors beats Paper
    elif(userValue == 'Paper' and cpuValue == 'Scissors'):
        print('CPU Wins!!')
    
    elif(userValue == 'Scissors' and cpuValue == 'Paper'):
        print('User Wins!!')


    elif(userValue == cpuValue):
        print('Draw!!')
    
    user_choice = input('\nCHOOSE Rock(R),PAPER(P),SCISSORS(S) OR (Q) TO QUIT: ')[0] #user choice
