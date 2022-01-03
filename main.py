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
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
elif choice == 2:
  print(scissors)
print("computer chooses:")
computer = random.randint(0, 2)
print(computer)
if computer == 0:
  print(rock)
elif computer == 1:
  print(paper)
elif computer == 2:
  print(scissors)

if choice == computer:
  print("It's a tie!")
if choice == 0 and computer == 1:
  print("You lose!")
elif choice == 1 and computer == 0:
  print("You win!")
if choice == 2 and computer == 0:
  print("You lose!")
elif choice == 0 and computer == 2:
  print("You win!")
if choice == 2 and computer == 1:
  print("You win!")
elif choice == 1 and computer == 2:
  print("You lose!")