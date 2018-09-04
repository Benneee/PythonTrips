#1 Introduce program to the user
#2 Request for pin
#2 Give the instruction to the user
#3 Ask user to select a valid option matching the operation they want to carry out on the machine
#4 Use if & elif statements and nested if statements if necessary to deliver all the options to the user


def main():

    #1 Introduce program to user
    introduction = 'Dear customer, you are welcome'
    print(introduction.title())

    #2 Request for pin
    pin = input('Please enter your pin: ')

    
    #Validation for pin
    if (len(pin) == 4) and (pin.isnumeric()):
        print('Thank you')
    else:
        exit(print('You entered a wrong pin'))

    #2 Give instruction to the user
    instruction = 'Please select the option matching the operation you want'
    print(instruction)

    #3 Ask user to select a valid option matching the operation they want to carry out on the machine
    action = input('What would you like to do today? \n (a) Withdrawal \n (b) Check balance \n (c) Transfer funds \n (d) Get airtime \n (e) Change card pin \n Please select your option: ').lower()

    #Use conditional statements to steer user forward

    #On selection of option a
    if action == 'a':
        amt = input('Select amount \n (i) 1000 \n (ii) 3000 \n (iii) 5000 \n (iv) 10000 \n (v) 20000 \n (vi) other \n please select the option with desired amount: ').lower()
        if amt == 'i':
            print('Please wait for your cash')
            print('Thank you, please take your cash')
        elif amt == 'ii':
            print('Please wait for your cash')
            print('Thank you, please take your cash')
        elif amt == 'iii':
            print('Please wait for your cash')
            print('Thank you, please take your cash')
        elif amt == 'iv':
            print('Please wait for your cash')
            print('Thank you, please take your cash')
        elif amt == 'v':
            print('Please wait for your cash')
            print('Thank you, please take your cash')
        elif amt == 'vi':
            entry = input('Please enter your desired amount: ')
            if (len(entry) <= 5) and (entry <= str(20000)) and (entry.isnumeric()):
                print('Thank you, please your cash')
            else:
                print('Insufficient balance')
        else:
            print('Insufficient balance')

    #On selection of option b
    elif action == 'b':
        print('Relax, if you get money inside this account, your money dey intact')

    #On selection of option c
    elif action == 'c':
        trans = input('Please enter the account number: ')
        if (trans.isnumeric()) and (len(trans) == 10):
            bank = input('Please enter acronym name of bank: ')
            if (bank.isalpha()) and (len(bank) == 3):
                print('Please confirm the account details')
                print('Account number and Bank name: ', trans, bank)
                cash = input('Please enter amount to transfer: ')
                if (cash.isnumeric()) and (len(cash) <= 5):
                    print('transfer successful')
                else:
                    print('Incomplete transaction, please try again later or check your balance')
            else:
                print('Incorrect entry, Please enter a valid bank name')
        else:
            print('please enter a valid account number')

    #On selection of option d
    elif action == 'd':
        network = input('Please select desired network \n (a) MTN \n (b) Airtel \n (c) Glo \n (d) 9mobile \n (e) ntel \n Please select desired option: ')
        if (network == 'a' or 'b' or 'c' or 'd' or 'e'):
            number = input('Please enter phone number: ')
            if (number.isnumeric()) and (len(number) == 11):
                amount = input('Please enter amount of airtime desired: ')
                if (amount.isnumeric()) and (len(amount) <= 4):
                    print('Transaction completed')
                else:
                    ('Insufficient balance or Invalid entry')
        else:
            print('Your network is unavailable, Thank you')


    #On selection of option e
    elif action == 'e':
        old_pin = input('Please enter old pin: ')
        if (old_pin == pin):
            new_pin = input('Please enter new pin: ')
            if (new_pin.isnumeric()) and (new_pin != old_pin):
                re_new_pin = input('Please re-enter new pin: ')
                if (re_new_pin == new_pin):
                    print('Pin changed successful')
                else:
                    print('New pin entries do not match')
            else:
                print('Invalid entry, You cannot use your old pin again')
        else:
            print('Please enter the valid old pin')

    restart = input('Do you wish to carry out another transaction: ').lower()
    if restart == 'yes':
        main()
    else:
        exit()

main()

