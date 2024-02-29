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

# Rock wins against scissors - Scissors wins against paper - Paper wins against rock


# Make a list with the choices corresponding to an index for the appropiate number choice
choices = [rock, paper, scissors]

# Save the player's input for their corresponding choice
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper, or 2 for scissors: \n"))

# Check to see if the input is valid (within range) and print the result
if 0 <= player_choice <= 2:
    print("You chose:")
    print(choices[player_choice])
else:
    print("Invalid choice")

# Make a random choice for the CPU
cpu_choice = random.randint(0, 2)

# Print the CPU's choice
print("Computer chose:")
print(choices[cpu_choice])

# Compare the player's choice with the CPU's choice to determine the outcome
if player_choice == cpu_choice:
    print("It's a draw.")
elif player_choice == 0:  # Player chooses Rock
    if cpu_choice == 2:
        print("You win! Rock crushes Scissors.")
    elif cpu_choice == 1:
        print("CPU wins! Paper covers Rock.")
elif player_choice == 1:  # Player chooses Paper
    if cpu_choice == 0:
        print("You win! Paper covers Rock.")
    elif cpu_choice == 2:
        print("CPU wins! Scissors cut Paper.")
elif player_choice == 2:  # Player chooses Scissors
    if cpu_choice == 1:
        print("You win! Scissors cut Paper.")
    elif cpu_choice == 0:
        print("CPU wins! Rock crushes Scissors.")
        
        
"""
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

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")

####### Debugging challenge: #########
#Try running this code and type 5.
#It will give you an IndexError and point to line 32 as the issue.
#But on line 38 we are trying to prevent a crash by detecting
#any numbers great than or equal to 3 or less than 0.
#So what's going on?
#Can you debug the code and fix it?
#Solution: https://repl.it/@appbrewery/rock-paper-scissors-debugged-end
"""
