#Investment value calculator
invest = float(input('Enter ur initial investment: '))
rate = float(input('Enter the annual rate of interest (in %): '))
years = float(input('Enter the no. of years of the investment: '))
value = invest*((1+(rate/100))**years)

print('The value after the given term is: ',value)