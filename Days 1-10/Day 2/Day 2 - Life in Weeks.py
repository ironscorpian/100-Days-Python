user_input = input("What is your current age? ")

user_input_converted = int(user_input)

weeks =  (90 *52) -(user_input_converted * 52)
months = (90 *12) - (user_input_converted * 12)
days = (90 *365) - (user_input_converted * 365)

print(f"You have {days}, {weeks} weeks and {months} months left")