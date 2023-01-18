# BMI 2.0 

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = (weight/(height*height))
R_bmi = round(bmi)

if(R_bmi < 18.5):
    print(f"Your BMI is {R_bmi}, you are underweight.")
elif(R_bmi > 18.5 and R_bmi < 25):
    print(f"Your BMI is {R_bmi}, you have a normal weight.")
elif(R_bmi > 25 and R_bmi < 30):
    print(f"Your BMI is {R_bmi}, you are slightly overweight.")
elif(R_bmi > 30 and R_bmi < 35):
    print(f"Your BMI is {R_bmi}, you are obese.")
else:
    print(f"Your BMI is {R_bmi}, you are clinically obese.")