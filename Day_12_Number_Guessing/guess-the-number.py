import random
logo= """"
   _____ _    _ ______  _____ _____   _______ _    _ ______   _   _ _    _ __  __ ____  ______ _____  
  / ____| |  | |  ____|/ ____/ ____| |__   __| |  | |  ____| | \ | | |  | |  \/  |  _ \|  ____|  __ \ 
 | |  __| |  | | |__  | (___| (___      | |  | |__| | |__    |  \| | |  | | \  / | |_) | |__  | |__) |
 | | |_ | |  | |  __|  \___ \\___ \     | |  |  __  |  __|   | . ` | |  | | |\/| |  _ <|  __| |  _  / 
 | |__| | |__| | |____ ____) |___) |    | |  | |  | | |____  | |\  | |__| | |  | | |_) | |____| | \ \ 
  \_____|\____/|______|_____/_____/     |_|  |_|  |_|______| |_| \_|\____/|_|  |_|____/|______|_|  \_\                                                                                                  
"""                                                                                    
attempts = 0

def thegame(): 
    print(logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    the_number = random.randint(1,100)
    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5
    
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        answer = int(input("Make a guess: "))
        if answer == the_number:
            print(f"You Got IT!! The number is {the_number}")
            exit()
        elif answer > the_number:
            print("Too high.\nGuess again.")
            attempts -= 1
        elif answer < the_number:
            print("Too low.\nGuess again.")
            attempts -= 1
    print("YOU LOSE :(")
    
thegame()
