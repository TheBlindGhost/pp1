hight = input('How tall are you?')
weight = input('How much do you weigh?')

a = float(hight)
b = float(weight)


bmi = b/(a**2)

c = bmi < 26

d = bmi > 18

e = c==d

print (f'Your BMI index: {bmi} Correct weight: {e}')