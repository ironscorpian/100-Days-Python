User_input = input("Which number do you want to check? ")
user_input_int = int(User_input)

if (user_input_int % 2) == 0:
    print(f"{user_input_int} is even")
else:
    print(f"{user_input_int} is odd")