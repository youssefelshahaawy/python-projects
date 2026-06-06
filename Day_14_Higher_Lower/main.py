import random
from art import*
from data import data


def formate_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{account["name"]}, a {account["description"]}, from {account["country"]}."


def check_answer(answer, a_followers, b_followers):
  """Checks followers against user's answer 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
  if a_followers > b_followers:
    return answer == "a"
  else:
    return answer == "b"


def game():
    print(logo)
    score = 0
    first = random.choice(data)
    secound = random.choice(data)
    game_continue = True
    while game_continue:
        first = secound
        secound = random.choice(data)
        while secound == first:
            secound = random.choice(data)
                
        print(f"Comare A: {formate_data(first)}")
        print(vs)
        print(f"Against B: {formate_data(secound)}")
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        firstfollowers = first["follower_count"]
        secoundfollowers = secound["follower_count"]
        is_correct = check_answer(answer,firstfollowers,secoundfollowers)
        
        print(logo)
        if is_correct:
            score += 1
            print(f"Nice! You got it! Your final score is {score}.")
        else:
            print(f"sorry,You lose! your final score is {score}.")
            game_continue = False


game()