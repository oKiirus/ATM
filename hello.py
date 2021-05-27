import os
import shutil

place = os.getcwd()

text = 'That Wasnt An Option :)'

choice = input('Enter 1 for creating a account 2 if otherwise: ')

if choice == '1':

    name = input('Enter Name Here: ')

    if os.path.exists(place + '/ATM') == False:

        os.mkdir(place + '/ATM')
        place = place + '/ATM'

    
 

    if os.path.exists(place + '/' + name) == False:
        os.makedirs(place + '/' + name)
        place = place + '/' + name
        os.chdir(place)


        file = open('Balance.txt', 'w')
        file.write('0')
        file.close
        text = 'Done!'

if choice == '2':
    
    name = input('Enter Name Here: ')

   

    choice = input('Enter 1 for withdrawing cash 2 for depositing and 3 for checking balance: ')

    if choice == '1':
        os.chdir(os.getcwd() + '/ATM' + '/' + name)

        amount = int(input('How much money would you like to withdraw? '))

        file = open('balance.txt', 'r')
        balance = int(file.read())
        
        file.close()
       
        

        if amount > balance:

            file = open('balance.txt', 'w')
            file.write('0')
            file.close
            text = 'Withdrew!'

        else:

            
            file = open('balance.txt', 'w')
            file.write(str(balance - amount))
            file.close
            text = 'Withdrew!'

        

    
    if choice == '2':
        os.chdir(os.getcwd() + '/ATM' + '/' + name)

        amount = input('How much money would you like to deposit? ')

        file = open('balance.txt', 'r')
        balance = file.read()
        file.close()
         
        file = open('balance.txt', 'w')
        file.write(str(int(balance) + int(amount)))
        file.close
        text = 'Deposited!'


    if choice == '3':

        os.chdir(os.getcwd() + '/ATM' + '/' + name)
        file = open('balance.txt', 'r')
        money = file.read()
        file.close()

       

        text = money




print(text)

        