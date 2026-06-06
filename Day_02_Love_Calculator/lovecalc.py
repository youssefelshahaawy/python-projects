print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?
# Your code below this line 👇
combined_names = name1 + name2
lower_names =combined_names.lower()
true = lower_names.count("t") + lower_names.count("r") + lower_names.count("u") + lower_names.count("e")
love = lower_names.count("l") + lower_names.count("o") + lower_names.count("v") + lower_names.count("e")
score = int(str(true) + str(love))

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
  print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")


# print("The Love Calculator is calculating your score...")
# name1 = input() # What is your name?
# name2 = input() # What is their name?
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇
# x = name1.lower()
# y = name2.lower()

# score1 = x.count('t') + x.count('r') + x.count('u') + x.count('e')
# score2 = y.count('t') + y.count('r') + y.count('u') + y.count('e')
# total = score1 + score2
# score3 = x.count('l') + x.count('o') + x.count('v') + x.count('e')
# score4 = y.count('l') + y.count('o') + y.count('v') + y.count('e')
# total2 = score3 + score4
 
# totalf = int(str(total) + str(total2))

# if totalf < 10 or totalf > 90:
#   print(f"Your score is {totalf}, you go together like coke and mentos.")
# elif totalf > 40 and totalf < 50:
#   print(f"Your score is {totalf}, you are alright together.")
# else:
#     print(f"Your score is {totalf}")