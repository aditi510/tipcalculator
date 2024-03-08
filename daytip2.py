print("Welcome to the tip calculator.")
total_bill= float(input("What was the total bill? $"))
tip_percent = int (input("What percentage tip would you like to give? 10,12,15?"))
tip_percentage= tip_percent/100
people= int(input("How many people to split the bill?"))
Pay= total_bill/people
Per_person= Pay*tip_percentage
final_amount=round(Per_person,2)
print(f"Each person should pay: ${final_amount}")
