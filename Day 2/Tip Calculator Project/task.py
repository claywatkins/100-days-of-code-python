from typing import final

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_percentage = tip * 0.01
bill_total = (bill * tip_percentage) + bill
final_split = round(bill_total / people, 2)

print(f"Each person should pay {final_split}")
