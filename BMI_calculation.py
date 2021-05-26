# Calculate Your Body Mass Index (BMI)
# Body mass index is a measure of body fat based on height and weight that applies to adult men and women.
# BMI categories adapted from website: https://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmi-m.htm


# Enter your height and weight using metric measures
height = float(input("Enter your height (in centimeters): ")) / 100
weight = float(input("Enter your weight (in kilograms): "))

# BMI calculation (kilogram per square meter)
bmi = weight / (height * height)
print("\nYour BMI is : ", round(bmi, 2))

if bmi < 18.5:
    print("You are categorised as: Underweight")
elif 18.5 < bmi < 24.9:
    print("You are categorised as: Normal weight")
elif 25.0 < bmi < 29.9:
    print("You are categorised as: Overweight")
elif bmi >= 30.0:
    print("You are categorised as: Obesity")
