#Quadratic equation solver
print('ax^2 + bx + c = 0')
a = float(input('Enter the value of a: '))
b = float(input('Enter the value of b: '))
c = float(input('Enter the value of c: '))

#the quadratic formula applied:
#brackets are used to bisect all the arithmetic so it is easier to understand
import math
d = math.sqrt(((b**2)-4*a*c))
#here it can be like this aaswell = d = (((b**2)-4*a*c)**(1/2))
x1 = (-b+d)/(2*a)
x2 = (-b-d)/(2*a)
print('ur answers are: ',x1,',',x2)