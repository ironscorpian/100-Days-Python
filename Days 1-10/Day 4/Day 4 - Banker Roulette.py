from random import randint


user_input = input("What are the names? Seperate them with a comma. ")

names = user_input.split(",")

names_len = len(names) - 1

random_num = randint(0, names_len)

random_person = names[(random_num)]

print(f"{random_person} will pay")
