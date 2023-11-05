buy = input('Buying price')
sell = input('Selling price')

buy = float(buy)
buy = round(buy,4)
sell = float(sell)
sell = round(sell,4)

diff = sell - buy
diff = round(diff,4)

print(diff)
