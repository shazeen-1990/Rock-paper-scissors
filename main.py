# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
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

#Write your code below this line 👇
images = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice >= 3 or choice <0 :
  print("You typed an invalid number,you lose!")
else:
  print(images[choice])
  #rock wins against scissors 0 2
  #scissors win against paper 2 1
  #paper wins against rock 1 0
  computer_choose = random.randint(0,2)
  print("Computer chose:")
  print(images[computer_choose])
  
  if choice == 0 and computer_choose == 2:
    print("You win!")
  elif computer_choose == 0 and choice == 2:
    print("You lose")
  elif computer_choose > choice:
    print("You lose")
  elif choice > computer_choose:
    print("You win")
  elif computer_choose == choice:
    print("it is a draw")