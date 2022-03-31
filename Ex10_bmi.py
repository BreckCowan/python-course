print("This program calculates your BMI.")



weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in inches: "))
bmi = weight / (height ** 2)

print("Your BMI is", round(bmi, 2))

if (bmi <= 18.5):
    classification = "underweight"
elif (bmi > 18.5 <= 24.9):
    classification = "normal weight"
elif (bmi > 25.0 <= 29.9):
    classification = "overweight"
else:
    classification = "obese"

print("Your BMI classification is", classification)