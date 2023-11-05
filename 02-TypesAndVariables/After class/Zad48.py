price = input('Enter price: ')
dis = input('Enter discount %: ')

price = float(price)
dis = float(dis)

dis_a = price * (dis/100)
dis_a = round(dis_a,2)
new = price - dis_a
new = round(price,2)

print(f'Price with discount: {new} Reduction: {dis_a}')