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
import random
print("Welcome to the game!")
graphic = [rock, paper, scissors]
choices = [0, 1, 2]
user_choice = int(input("Type 0 for Rock, 1 for Paper, and 2 for Scissors\n"))
computer_choice = random.choice(choices)
if user_choice > computer_choice:
    if user_choice > 2:
        print("Invalid number")
    elif user_choice != 1:
        print(f"User choice {graphic[user_choice]} \n Computer choice {graphic[computer_choice]} \n COMPUTER WON!")
    else:
        print(f"User choice {graphic[user_choice]} \n Computer choice {graphic[computer_choice]} \n YOU WON!")
elif user_choice < computer_choice:
    if computer_choice != 1:
        print(f"User choice {graphic[user_choice]} \n Computer choice {graphic[computer_choice]} \n YOU WON!")
    else:
        print(f"User choice {graphic[user_choice]} \n Computer choice {graphic[computer_choice]} \n COMPUTER WON!")
elif user_choice == computer_choice:
    print(f"User choice {graphic[user_choice]} \n Computer choice {graphic[computer_choice]} \n DRAW!")
