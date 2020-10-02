mass = float(input('Enter your weight (kg): '))
height = float(input('Enter your height (cm): ')) / 100

bmi = mass / (height * height)

if bmi >= 30:
    print(bmi, 'You are Obese')
elif bmi >= 25 and bmi < 30:
    print(bmi, 'You are Overweight')
elif bmi >=18.5 and bmi < 25:
    print(bmi, 'You are Normal')
elif bmi >= 16 and bmi < 18.5:
    print(bmi, 'You are Underweight')
else:
    print(bmi, 'You are Severely')
