"""
# 1. Create a greeting for your program.
greeting = "Welcome to Band Name Generator, We'll help you pick the best name for your up and coming Band!\n"
print(greeting)
# 2. Ask the user for the city that they grew up in.
city_name = input("What city did you grow up in?\n")
# 3. Ask the user for the name of a pet.
pet_name = input("What is the name of your pet?\n")
# 4. Combine the name of their city and pet and show them their band name.
band_name = f"Your band name could be: The {city_name} {pet_name}(s)!!!\n"
# 5. Make sure the input cursor shows on a new line:
print(band_name)
# Solution: https://replit.com/@appbrewery/band-name-generator-end
"""
print("Welcome to Band Name Generator. We'll help you pick the best name for your up and coming Band!\n")
print("This program helps you generate a unique band name based on a few of your personal preferences.")

while True:
    city_name = input("What city did you grow up in?\n").title()
    pet_name = input("What is the name of your pet?\n").title()
    band_name = f"Your band name could be: The {city_name} {pet_name}(s)!!!"
    print(band_name)

    continue_generation = input("Do you want to generate another Band Name? (Yes/No)\n")
    if continue_generation.lower() == "no":
        print("Thank you for using the Band Name Generator. Enjoy your brand new Band Name. Have a great day!")
        break
