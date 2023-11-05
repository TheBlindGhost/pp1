num = input('Write an amount')

a = float(num)
b = round(a,2)

vat = b*(23/100)
vat1 = round(vat, 2)

print(f'Amount : {b} VAT 23% : {vat1}')