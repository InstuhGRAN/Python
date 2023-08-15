#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percent = float(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
people = float(input("How many people to split the bill?\n"))
total = float((bill + (bill * (percent/100))) / people)
new_total = float(round(total, 2))
new_total = "{:.2f}".format(total)
print(f'Each person should pay ${new_total}')