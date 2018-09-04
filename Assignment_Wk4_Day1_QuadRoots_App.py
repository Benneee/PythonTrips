#The Quadratic Roots Programme

#ALGORITHM

#1 Introduce the program to the user

#2 Give the required instructions to run program appropriately

#3 Request values for a, b, c

#4 Define a variable for the discriminant
#- Solve the discriminant
#- Solve the square root of the discriminant 
#- import math module and do the print thingy

#5 Define variables for r1 and r2

#6 Define the conditional statements;
#- discriminant > 0
#- discriminant < 0
#- discriminant == 0

#- Implement the calculation for the two roots when discriminant > 0




#The Program
#1 Introduce the program to the user
greeting = 'welcome to the quadratic roots programme'
print(greeting.title())

#2 Give the required instructions to run program appropriately
instruction = 'please provide values where required'
print(instruction.title())

#3 Request values for a, b, c
a = float(int(input('Please provide a value for a:  ')))
b = float(int(input('Please provide a value for b:  ')))
c = float(int(input('Please provide a value for c:  ')))

#4 Define a variable for the discriminant
d = 'discriminant'

#- Solve the discriminant
d = float(int((b ** 2) - (4 * a * c)))
print('The discriminant is ' + str(d))

#- Solve the square root of the discriminant 
#- import math module and do the print thingy

import math
print('The square root of the discriminant is ' + str(math.sqrt(abs(float(d))))) 
#The abs function returns the absolute value of d which can be negative depending on the values of a, b and c.
#The python math module sqrt method has a problem with negative values.


#5 Define variables for r1 and r2
r1 = float((-b) + (d) / (2 * a))
r2 = float((-b) - (d) / (2 * a))

#6 Define the conditional statements;
#- discriminant > 0
if d > 0:
	print('The equation has two real roots: ' + str(r1) + ' and ' + str(r2))
#- Implement the calculation for the two roots when discriminant > 0

#- discriminant == 0
elif d == 0:
	print('The equation has only one real root')

#- discriminant < 0
else:
	print('The equation has no real root')

print('Thank you for using this app')
