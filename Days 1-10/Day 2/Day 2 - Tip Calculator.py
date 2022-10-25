print("Easy Tip Calculator")

total_bill_input = input("What was the total bill? ")
total_bill_float = float(total_bill_input)

percentage_input = input("What percentage would you like to give? 10, 12 or 15? ")
percentage_input_int = int(percentage_input)

num_people_input = input("How many people are there? ")
num_people_input_int = int(num_people_input)

percentage = 1 + (percentage_input_int/100)
final = (total_bill_float * percentage)/ num_people_input_int
rounding_final = round(final, 2)

print(f"Each person will pay: {rounding_final}")