"""
Instructions
Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill.

Small pizza (S): $15

Medium pizza (M): $20

Large pizza (L): $25

Add pepperoni for small pizza (Y or N): +$2

Add pepperoni for medium or large pizza (Y or N): +$3

Add extra cheese for any size pizza (Y or N): +$1

Example Input
L
Y
N
Example Output
Thank you for choosing Python Pizza Deliveries!
Your final bill is: $28.
"""
"""
print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size Pizza do you want? S, M, or L \n: ").lower() # What size pizza do you want? S, M, or L
add_pepperoni = input("Would you like to add extra Pepperoni? Y or N\n: ").lower() # Do you want pepperoni? Y or N
extra_cheese = input("Would you like to add some extra Cheese? Y or N\n: ").lower() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
valid_sizes = ['s', 'm', 'l']
while size not in valid_sizes:
  print("Invalid size. Please enter S, M, or L.")
  size = input("What size Pizza do you want? S, M, or L: ").lower()

valid_pepperoni = ["y", "n"]
while add_pepperoni not in valid_pepperoni:
  print("Invalid choice. Pleaser enter Y or N")
  add_pepperoni = input("Would you like to add extra Pepperoni? Y or N\n: ").lower()
  
valid_cheese = ["y", "n"]
while extra_cheese not in valid_cheese:
  print("Invalid choice. Please enter Y or N")
  extra_cheese = input("Would you like to add some extra Cheese? Y or N\n: ").lower()
  
bill = 0

if size == "S":
  bill += 15
  if add_pepperoni == "Y":
    bill += 2

elif size == "M":
  bill += 20
  if add_pepperoni == "Y":
    bill += 3
  
elif size == "L":
  bill += 25
  if add_pepperoni == "Y":
    bill += 3
    
if extra_cheese == "Y":
  bill += 1
  
print(f"Your final bill is: ${round(bill, 2)}")
#print(f"Your final bill is: ${bill}.")
"""
"""
Angela's Solution

bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3
    
if extra_cheese == "Y":
  bill += 1
  
print(f"Your final bill is: ${bill}.")

"""
#ChatGPT Solution
print("Welcome to the Python Pizza Deliveries!")

# Validate size input
valid_sizes = ['s', 'm', 'l']
size = input("What size Pizza do you want? S, M, or L: ").lower()
while size not in valid_sizes:
    print("Invalid size. Please enter S, M, or L.")
    size = input("What size Pizza do you want? S, M, or L: ").lower()

# Validate add_pepperoni input
valid_pepperoni = ["y", "n"]
add_pepperoni = input("Would you like to add extra Pepperoni? Y or N: ").lower()
while add_pepperoni not in valid_pepperoni:
    print("Invalid choice. Please enter Y or N")
    add_pepperoni = input("Would you like to add extra Pepperoni? Y or N: ").lower()

# Validate extra_cheese input
valid_cheese = ["y", "n"]
extra_cheese = input("Would you like to add some extra Cheese? Y or N: ").lower()
while extra_cheese not in valid_cheese:
    print("Invalid choice. Please enter Y or N")
    extra_cheese = input("Would you like to add some extra Cheese? Y or N: ").lower()

# Calculate bill
bill = 0

if size == "s":
    bill += 15
    if add_pepperoni == "y":
        bill += 2
elif size == "m":
    bill += 20
    if add_pepperoni == "y":
        bill += 3
elif size == "l":
    bill += 25
    if add_pepperoni == "y":
        bill += 3

if extra_cheese == "y":
    bill += 1

print(f"Your final bill is: ${bill:.2f}")

