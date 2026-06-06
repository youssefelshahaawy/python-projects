logo = '''


                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
 
members = []
x = True
while x:
    auction_members = {}
    name = input("what's your name? ")
    bid = int(input("what's your bid? $"))
    auction_members["name"] = name
    auction_members["bid"] = bid
    members.append(auction_members)
    end = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if end == "no":
        x = False

highest_bid = 0
winner_name = ""
for member in range(0,len(members)):
    if members[member]["bid"] > highest_bid:
        highest_bid = members[member]["bid"]
        winner_name = members[member]["name"]

print(f"The Winner is {winner_name} with a bid of ${highest_bid}!")