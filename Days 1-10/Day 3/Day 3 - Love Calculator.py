
print("Love Calculator")

name1 = (input("What is your name? ")).lower()
name2 = (input("What is their name? ")).lower()

T = name1.count("t")+ name2.count("t")
R = name1.count("r")+ name2.count("r")
U = name1.count("u")+ name2.count("u")
E = name1.count("e")+ name2.count("e")
true_total = T+R+U+E

L = name1.count("l") + name2.count("l")
O = name1.count("o") + name2.count("o")
V = name1.count("v") + name2.count("v")
E = name1.count("e") + name2.count("e")
love_total = L+ O + V + E

total_string = str(true_total) + str(love_total)
total = int(total_string)



if total < 10 or total > 90:
    print(f"Your love score is {total_string}, you go together like coke and mentos.")
elif (total >= 40) and (total <= 50):
    print(f"Your love scoreis {total_string}, you are alright together")
else:
    print(f"Your love score is {total_string}")
