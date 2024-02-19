"""

Instructions
I was reading this article by Tim Urban - Your Life in Weeks(https://waitbutwhy.com/2014/05/life-weeks.html) and realised just how little time we actually have.

Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x weeks left.
Where x is replaced with the actual calculated number of weeks the input age has left until age 90.

Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

Example Input
56
Example Output
You have 1768 weeks left.

"""

"""
# MY SOLUTION
age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
limit_age = 90

years_remaining = limit_age - int(age)

weeks_in_year = 52
# weeks_in_month = 4

# days_in_year = 365
# days_in_month = 30
# days_in_week = 7

# hours_in_day = 24
# minutes_in_hour = 60
# seconds_in_minute = 60

weeks_left_to_live = weeks_in_year * years_remaining
# print(f"You have {weeks_left_to_live} weeks left to live!")
print(f"You have {weeks_left_to_live} weeks left")
"""

# Angela's Solution
age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
years = 90 - int(age)
weeks = years * 52
print(f"You have {weeks} weeks left.")
