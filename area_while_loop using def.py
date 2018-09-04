#ALGORITHM
#1 Introduce the program to the user

#2 Define instructions to the user

#3 Request for a shape entry from user

#4 Use conditional statements to run procedure for area calculation



#The Program
def main():

        #1 Introduce the program to the user
        greeting = 'welcome to the area calculator app'
        print(greeting.title())


        #2 Define instructions to the user
        instruction = 'select the option that matches your desired shape'
        print(instruction.title())


        #3 Request for a shape entry from user
        shape_request = input('Please select your desired shape:\n (a) square \n (b) rectangle \n (c) triangle \n shape choice: ').lower()


        #4 Use conditional statements to run procedure for area calculation
        if shape_request == 'a':
                l_sq = input('Please enter length of square: ')
                area = int(l_sq) ** 2
                print('The area of the square is ', area)


        elif shape_request == 'b':
                l_rec = input('Please enter length of rectangle: ')
                b_rec = input('Please enter breadth of rectangle: ')
                rec_area = int(l_rec) * int(b_rec)
                print('The area of the rectangle is ', rec_area)

        elif shape_request == 'c':
                base = input('Please enter base of triangle: ')
                height = input('Please enter height of triangle: ')
                triangle_area = float(0.5) * float(base) * float(height)
                print('The area of the triangle is ', triangle_area)


        else:
                print('You have selected an invalid option')

        #To run the program again 
        restart = input('Do you wish to restart? ').lower()
        if restart.lower() == 'yes':
                main()

        else:
                exit()

main()


