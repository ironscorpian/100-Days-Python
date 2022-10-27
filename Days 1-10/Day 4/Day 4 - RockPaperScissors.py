import random

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

game_image = [rock, paper, scissors]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n "))
computer_input = random.randint(0,2)

computer_output = game_image[computer_input]

print(game_image[user_input])
print(f"Computer chose: {computer_output}")

if computer_output == user_input:
    print("It's A Draw")
elif user_input == 0 and computer_input == 1:
  print("You loose")
elif user_input == 0 and computer_input == 2:
  print("You win")
#User is paper
elif user_input == 1 and computer_input == 2:
  print("You loose")
elif user_input == 1 and computer_input == 0:
  print("You win")
#User is scissors
elif user_input == 2 and computer_input == 0:
  print("You loose")
elif user_input == 2 and computer_input == 1:
  print("You win")
else:
  print("You typed in an invalid number")
  