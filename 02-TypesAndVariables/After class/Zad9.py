a = 160

inch = a*0.393701
feet = inch/12
f1 = int(feet)
f2 = round(inch%12)

print(f'I am 170cm tall, i.e. {f1} feet and {f2} inches')