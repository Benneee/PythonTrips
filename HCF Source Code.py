print("number tester")
number = int(input('enter number, '))
             
if(number % 2 == 2):
	print (number, 'is an odd number')
elif(number % 2 == 1):
	print (number, 'is an odd number')	
else:
	print (number, 'is an even number')


newYear = int(input('enter year; '))
result1 = newYear % 4
result2 = newYear % 400

if result1 == 0:
	print(newYear, 'is a leap year')
elif result2 == 0:
	print(newYear, 'is a leap year')
else:
	print(newYear, 'is not a leap year')

