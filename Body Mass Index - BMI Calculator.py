#Creating A BMI Calculator

print('This is a BMI - Body Mass Index - Calculator')

instruction = "please provide the following information accordingly - weight in kilograms, height in metres"
print(instruction.title())

#Requirements
weight = float(input('Please enter your weight:  '))

height = float(input('Please enter your height:  '))


#The BMI Calculation Part
bmi = float(weight / (height ** 2))

#Rounding up the bmi to 1 decimal place
bmi = round(bmi, 1)

#Displaying the BMI
print(bmi)

#Conditional Statements For BMI
if (bmi < 18.5):
    print('Please, eat more food, You are Underweight!')

elif (bmi >= 18.5) and (bmi < 25):
    print('Your Body Mass Index is Normal')

elif (bmi >=25) and (bmi < 30):
    print('You are Overweight')

else:
    print('There\'s no better way to say this; You are Obese!')

#End of Code
greeting = "Thank you for using this app"
print(greeting.upper())

