num = input('Registration number?')
st = str(num)

a1 = 'KK' in st 
a2 = 'KR' in st

a3 = a1 + a2

t = a3>0

print(f'Car from Kraków: {t}')