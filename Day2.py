#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
# or total_bill_in_float = float(total_bill), then without the float at the start

tip = int(input("How much would you like to give? 10, 12, or 15? "))
# or tip_in_int = int(tip), then without the int at the start

num_people = int(input("How many people to split the bill? "))
# or num_people_in_int = int(num_people), then without the int at the start

# if you used the commented text, variables are named differently latter

tip = (tip/ 100) + 1
amount = (total_bill / num_people) * tip

rounded_bill = round(amount, 2)
print(f"Each person should pay: ${rounded_bill}")