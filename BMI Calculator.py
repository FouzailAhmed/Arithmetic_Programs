
#BMI calculator working
weight = 0
height = 0
BMI = 0

weight = float(input('please enter ur body weight in kilograms:'))
height = float(input('please enter ur height in meters:'))
#before the calculation of bmi it should be noted that the inout taken was converted into float
BMI = (weight/height**2)
print('ur current BMI is:',BMI)


