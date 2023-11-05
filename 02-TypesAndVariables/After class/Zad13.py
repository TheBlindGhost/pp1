a = input('Side 1:')
b = input('Side 2:')
c = input('Side 3:')
a1 = int(a)
b1 = int(b)
c1 = int(c)
cir = a1+b1+c1
s = cir/2
area = s*(s-a1)*(s-b1)*(s-c1)
area1 = area**(1/2)
print (f'Triangle area: {area1} Triangle circumference: {cir}')
