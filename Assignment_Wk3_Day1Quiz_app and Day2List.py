#Assignment For Week 3, Day 1
#Introduction to the trivia
print('Welcome to the Benneee_ Python Trivia')

#Instructions For The Trivia
print('Answer all questions correctly by choosing the right option')

print('Good Luck')

#Initialise the score to 0
score = 0

#This causes a rerun of the questions if the user does not answer ALL the questions correctly
while score < 5:
    


    #The Questions
    question_1 = input("""(1) Python is a programming language that is interpreted and not compiled \n (a) True \n (b) False \n (c) Can not say \n please enter your answer: """)
    a = 'correct'

    #Conditions for the answers provided
    if (question_1.lower() == 'a'):
        print('CORRECT')
        score +=1
        
    else:
        print('WRONG')
        score -=1
        

    question_2 = input("""(2) Python can be used for data science and analytics \n (a) True \n (b) False \n (c) Can not say \n please enter your answer: """)
    a = 'correct'

    #Conditions for the answers provided
    if (question_2.lower() == 'a'):
        print('CORRECT')
        score +=1
        
    else:
        print('WRONG')
        score -=1
        

    question_3 = input("""(3) Python can be used on its own to create webpages like HTML & CSS \n (a) True \n (b) False \n (c) Can not say \n please enter your answer: """)
    b = 'correct'

    #Conditions for the answers provided
    if (question_3.lower() == 'b'):
        print('CORRECT')
        score +=1

    else:
        print('WRONG')
        score -=1
        

    question_4 = input("""(4) A degree in Computer Science is very important to learn how to code \n (a) True \n (b) False \n (c) Can not say \n please enter your answer: """)
    b = 'correct'

    #Conditions for the answers provided
    if (question_4.lower() == 'b'):
        print('CORRECT')
        score +=1
    else:
        print('WRONG')
        score -=1

    question_5 = input("""(5) Python is an Object Oriented Programming Language \n (a) True \n (b) False \n (c) Can not say \n please enter your answer: """)
    a = 'correct'

    
    if (question_5.lower() == 'a'):
    #Conditions for the answers provided
        print('CORRECT')
        score +=1
        
    else:
        print('WRONG')
        score -=1
        

    print('Your score is', score, '/5')
    if score < 5:
        print('Sorry, You have to take the test again')
        score = 0






#Assignment For Week 3, Day 2

#The range function provides a list of numbers from 0 to 21, leaving out 21 from the mix even if the condition was not for even numbers
even_numbers = list(range(0, 21, 2))

#The "for loop" runs through the numbers and returns an iteration of the even numbers as long as the condition remains true
for even_number in even_numbers:
	print (even_number)


#Assignment For Week 3, Day 2
#The approved way to do the even numbers 
numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

#A "for loop" incorporating an "if statement" to print the even number from the list above
for number in numbers:
    if number % 2 == 0:
        print(number)
    
    

 
