print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#Write your code below this line 👇

# ChatGPT Solution
# def get_user_choice(prompt, options):
#     user_input = input(prompt).lower()
#     while user_input not in options:
#         print(f"Invalid choice. Please enter one of the following: {', '.join(options)}")
#         user_input = input(prompt).lower()
#     return user_input

# # Crossroad choice
# crossroad = get_user_choice("You are at a crossroad, where do you want to go? Type 'left' or 'right': ", ['left', 'right'])
# if crossroad == "left":
#     # Lake choice
#     lake = get_user_choice("You come to a lake with an island in the middle. Type 'wait' to wait for a boat or 'swim' to swim across: ", ['wait', 'swim'])
#     if lake == "wait":
#         # Island choice
#         island = get_user_choice("You arrive at the island unharmed. There is a house with 3 doors: one red, one yellow, and one blue. Which color do you choose? ", ['red', 'yellow', 'blue'])
#         if island == "red":
#             print("You enter a room full of fire. Game Over.")
#         elif island == "yellow":
#             print("You found the treasure! You Win!")
#         else:  # Blue door
#             print("You enter a room of beasts. Game Over.")
#     else:  # Swim
#         print("You get attacked by an angry trout. Game Over.")
# else:  # Right at crossroad
#     print("You fell into a hole. Game Over.")


"""
# My horrible solution

crossroad = input("You are at a crossroad, where do you want to go? Type 'left' or 'right' \n:").lower()
if crossroad == "right":
  print("Game Over")
elif crossroad == "left":
  print("Great, you made it to a lake!")
  
lake = input("You come to a lake, there is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across \n:").lower()
if lake == "swim":
  print("You drown trying to swim to the middle of the lake. Game Over")
elif lake == "wait":
  print("You make it to an island in the middle of the lake.")
  
island_house_door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? Type 'red', 'yellow' or 'blue' \n:").lower()

if island_house_door == "red":
  print("You enter and the entire place is on fire. You are burnt to death. Game Over")
elif island_house_door == "blue":
  print("You fall into a deep well and break both your arms and legs. The well quickly fills up with water and you drown. Game Over")
elif island_house_door == "yellow":
  print("You make it into a beautiful room full of gold, diamonds, and other treasure everywhere. You have found the treasure of Treasure Island, Congratulations You Win!")

"""

"""
# Angela's Solution

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Write your code below this line 👇

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")

"""

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

def make_choice(prompt, choices):
    user_choice = input(prompt).lower()
    while user_choice not in choices:
        print("Invalid choice. Please choose again.")
        user_choice = input(prompt).lower()
    return user_choice

# Adding more choices
crossroad = make_choice("You are at a crossroad. Where do you want to go? Type 'left', 'right', or 'straight': ", ['left', 'right', 'straight'])

if crossroad == 'left':
    # Original left path
    lake = make_choice("You've come to a lake. There's an island in the middle. Type 'wait' for a boat or 'swim' to swim across: ", ['wait', 'swim'])
    if lake == 'wait':
        door = make_choice("You arrive at the island unharmed. There's a house with 3 doors: red, yellow, and blue. Which do you choose? ", ['red', 'yellow', 'blue'])
        if door == 'red':
            print("Room full of fire. Game Over.")
        elif door == 'yellow':
            print("You found the treasure! You Win!")
        else:
            print("Room of beasts. Game Over.")
    else:
        print("Attacked by a trout. Game Over.")
elif crossroad == 'right':
    print("You fell into a hole. Game Over.")
else:  # New straight path
    maze = make_choice("You find a maze with two entrances. Do you enter 'left' or 'right' entrance? ", ['left', 'right'])
    if maze == 'left':
        print("You're lost in the maze forever. Game Over.")
    else:
        print("You found a shortcut to the treasure! You Win!")

# Add more paths and scenarios to expand the game further.
