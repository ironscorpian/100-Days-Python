from random import weibullvariate


user_input_weight = float(input("What is your weight in kg? "))
user_input_height = float(input("What is your hegith in m? "))

# height_cm = user_input_height/100 if you want to use height in cm
BMI = user_input_weight/(user_input_height**2)

print("Your bmi is: ", BMI)