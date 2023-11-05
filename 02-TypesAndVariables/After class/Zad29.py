import random

x = random.randrange(1,6)

a = input('Guess the number')

b = int(a)

c = x==b

print(c, 'Right number:', x)