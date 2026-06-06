with open("Input/Names/invited_names.txt","r") as file:
    names = file.readlines()
    names_withou_space = []
    for name in names:
        names_withou_space.append(name.strip())
    
with open("Input/Letters/starting_letter.txt","r") as letter:
    x = letter.read()
    for name in names_withou_space:
       new_letters = (x.replace("[name]",name))
       with open(f"./Output/ReadyToSend/{name}'s_letter.txt",mode="w") as f:
           f.write(new_letters)
           