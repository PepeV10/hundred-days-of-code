"""
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

It should look something like this:

Welcome to the tip calculator.
What was the total bill? $124.56
What percentage tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 7
Each person should pay: $19.93

#Write your code below this line 👇
"""

"""
#My Solution
print("Welcome to the tip calculator.")
total_bill = float(input(f"What was the total bill? $"))
percentage_tip = float(input(f"What percentage tip would you like to give? 10%, 12%, 15%, 20%, 25%? "))
total_people = int(input(f"How many people to split the bill? "))
final_amount_per_person = (total_bill / total_people) * (1 + (percentage_tip / 100))
print(f"Each person should pay: ${final_amount_per_person:.2f}")
"""

#Angela's Solution
print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")