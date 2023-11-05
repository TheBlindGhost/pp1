#asking for temperature
temp = input("What is the temperature in celsius?")
#converting to int
cal = float(temp)
#Calculating kelvin
kelvin = cal + 273.15
#Calculating farenheit
far = (cal * 9/5) + 32
#Displaying data
print(f'That is {kelvin} degrees Kelvin and {far} degrees Fahrenheit!' )