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

#Write your code below this line 👇
import random

rock_paper_scissors = [rock, paper, scissors]

pick = int(input("What do you want to choose? Pick 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

if pick >= 3 or pick < 0:
    print("Invalid pick, you lose automatically.")
else:
    print(rock_paper_scissors[pick])
    print("\nComputer chose:\n")
    computers_pick = random.randint(0, 2)
    print(rock_paper_scissors[computers_pick])

    if pick == 0 and computers_pick == 0:
        print("It's a tie.")
    elif pick == 0 and computers_pick == 1:
        print("Computer wins.")
    elif pick == 0 and computers_pick == 2:
        print("You win.")
    elif pick == 1 and computers_pick == 1:
        print("It's a tie.")
    elif pick == 1 and computers_pick == 0:
        print("You win.")
    elif pick == 1 and computers_pick == 2:
        print("Computer wins.")
    elif pick == 2 and computers_pick == 2:
        print("It's a tie.")
    elif pick == 2 and computers_pick == 0:
        print("Computer wins.")
    elif pick == 2 and computers_pick == 1:
        print("You win.")