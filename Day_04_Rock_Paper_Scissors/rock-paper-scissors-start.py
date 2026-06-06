# import random
# choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# choices = ["rock", "paper", "scissors"]
# if choice == 0:
#     print(rock)
# elif choice == 1:
#     print(paper)
# else:
#     print(scissors)
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if  user_choice > 2:
    print("Invalid number")
    exit()

print(images[user_choice])
computer_choice = random.randint(0,2)
print("Computer chose:")
print(images[computer_choice])

if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 2 and computer_choice == 0:
    print("You lose!")

elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
else:
    print("It's a draw!")