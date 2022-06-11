import random

print('ROCK, PAPER SCISSORS GAME!')
print('Here are the Rules :')
print('Rock smashes Scissors')
print('Paper covers Rock')
print('Scissors cut Paper')
print("Let's Start!")

options = ['R', 'P', 'S']
while True:

    user = input('Enter a choice (R for Rock , P for Paper, S for Scissors) : ').upper()
    if user not in options:
        print("Input is invalid!")
    else:
        pass
        userChoice = ''

        if user == "R":
            userChoice = 'Rock'
        elif user == "S":
            userChoice = 'Scissors'
        elif user == "P":
            userChoice = 'Paper'

        computer = random.choice(options)
        computerChoice = ""

        if computer == "R":
            computerChoice = "Rock"
        elif computer == "S":
            computerChoice = "Scissors"
        elif computer == "P":
            computerChoice = "Paper"

        print(f"Player ({userChoice}) : CPU ({computerChoice})")

        if user == "R":
            if computer == 'S':
                print('Rock smashes Scissors , You WIN!')
            elif computer == "P":
                print('Paper cover Rock, Computer WINS!')
        elif user == 'S':
            if computer == 'P':
                print('Scissors cuts Paper , You WIN!')
            elif computer == "R":
                print('Rock smashes Scissors, Computer WINS!')
        elif user == 'P':
            if computer == 'R':
                print('Paper covers rock, You WIN!')
            elif computer == "S":
                print('Scissors cuts paper, Computer wins!')
        if user == computer:
            print('This is a TIE!,play again!')
        else:
            print('Thanks for playing!')
            break
