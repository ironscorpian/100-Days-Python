
user_input_weight = int(input("What is your weight in kg? "))
user_input_height = int(input("What is your hegith in m? "))

# height_cm = user_input_height/100 if you want to use height in cm
BMI = user_input_weight/(user_input_height**2)

print(BMI)

if BMI < 18.5:
    print("You are underweight")
elif BMI <= 25 :
    print("You are normal weight")
elif BMI <= 30:
    print("You are overweight")
elif BMI <= 35:
    print("You are obese")
else:
    print("You are clinically obese")
