import random
while True :
    user = str(input('what is your choise *p* for paper, *r* for rock, *s* for scissors : '))
    if user == 'p' or user =='s' or user =='r':
        computer = random.choice(['p', 'r', 's'])
        print(computer)
        if computer == user :
            print('tie')
        elif (computer == 'p' and user == 'r') or (computer == 'r' and user == 's') or (computer == 's' and user == 'p'):
            print('computer win')
        else:
            print('you win')
    else:
        print("please enter a right vaule and try again ")
