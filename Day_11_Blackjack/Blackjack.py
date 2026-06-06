# file:///C:/Users/Admin/Downloads/Blackjack_Flowchart.pdf
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
your_cards = []
computer_cards = []
your_cards.append(random.choice(cards))
computer_cards.append(random.choice(cards))
computer_cards.append(random.choice(cards))

def dealcard():
    cont = True
    print("welcome to the blackjack game")
    print(logo)
    while cont :
        your_cards.append(random.choice(cards)) 
        Sum = 0
        Sum += sum(your_cards)
                
        if 11 in your_cards and Sum > 21:
            Sum -= 10

        if Sum == 21:
            print("BLACK JACK!!\n YOU WIN!!")
            exit()

        print(f"Your cards {your_cards},current score = {Sum}")
        print(f"Computer's first card is [{computer_cards[0]}]")

        if Sum > 21:
            print("YOU LOSE!!")
            exit()

        answer = input(f"Type 'y' to get another card, type 'n' to pass: ")
        
        if answer != 'y':
            cont = False
            
    Sum_computer = 0
    Sum_computer += sum(computer_cards)
    if Sum_computer == 21:
            print("Computer BLACK JACK!!\n YOU LOSE!!")
            exit()

    while Sum_computer < 17:
        computer_cards.append(random.choice(cards))
        Sum_computer += computer_cards[-1]
        if 11 in computer_cards and Sum > 21:
            Sum_computer -= 10
        
    print(f"Your final cards:{your_cards}, final score: {Sum}")
    print(f"Computer's final score:{computer_cards}, final score: {Sum_computer}")
    if Sum_computer > 21:
            print("YOU WIN!!")
            exit()
    if Sum > Sum_computer:
        print("You win!")
    elif Sum < Sum_computer :
        print("You Lose :(")
    else:
        print("DRAW")

dealcard()