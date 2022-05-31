import time
import crud
import os

def mainMenu():
    print('---------Main Menu-----------')
    print('Enter following:')
    print('---------------------------')
    print('Enter 1 to add new Patient')
    print('Enter 2 to view Patient\'s list')
    print('Enter 3 to add new Doctor')
    print('Enter 4 to view Doctor\'s list')
    print('Enter 5 to quit the program.')
    print('---------------------------')
    check = False
    while check is not True:
        v = str(input('Enter from above options: ')).lower()
        if v == '1':
            check = True
            newBill()
        elif v == '2':
            check = True
            listMenu('p')
        elif v == '3':
            check = True
            newDoctor()
        elif v == '4':
            check = True
            listMenu('d')
        elif v == '5':
            check = True
            star = '*'
            print('---------------------------')
            print(f'Good bye! Clearing Console....')
            for i in range(3):
                print(star)
                star += star
                time.sleep(0.8)
            print('---------------------------')
            os.system('cls' if os.name == 'nt' else 'clear')
            pass
        else:
            print('------------------------------------------------------')
            print('Error! Invalid value.')
            print('------------------------------------------------------')


def newDoctor():
    c = crud.CRUD()
    a = c.addDoctor()
    if a == 'y':
        check = False
        while check is not True:
            v = str(input('Add another Doctor? (y/n): '))
            if v == 'y':
                newDoctor() # callback itself to add another doctor
                check = True # exit the loop
            elif v == 'n':
                check = True # exit the loop
                mainMenu()
            else: 
                print('------------------------------------------------------')
                print('Error! Invalid value.')
                print('------------------------------------------------------')
    elif a == 'n':
         while check is not True:
            v = str(input('Add Doctor? (y/n): '))
            if v == 'y':
                newDoctor() # callback itself to add another doctor
                check = True # exit the loop
            elif v == 'n':
                check = True # exit the loop
                mainMenu()
            else: 
                print('------------------------------------------------------')
                print('Error! Invalid value.')
                print('------------------------------------------------------')
    del c,a # delete CRUD instance

def newBill():
    c = crud.CRUD()
    a = c.addPatient()
    if a == 'y':
        printBill(c.getID())
        check = False
        while check is not True:
            v = str(input('Add another patient? (y/n): '))
            if v == 'y':
                newBill() # callback itself to add another patient
                check = True # exit the loop
            elif v == 'n':
                check = True # exit the loop
                mainMenu() # exit to main menu
            else: 
                print('------------------------------------------------------')
                print('Error! Invalid value.')
                print('------------------------------------------------------')
    elif a == 'n':
         while check is not True:
            v = str(input('Add another patient? (y/n): '))
            if v == 'y':
                newBill() # callback itself to add another patient
                check = True # exit the loop
            elif v == 'n':
                check = True # exit the loop
                mainMenu()
            else: 
                print('------------------------------------------------------')
                print('Error! Invalid value.')
                print('------------------------------------------------------')
    del c,a # delete CRUD instance

def printBill(id):
    star = '*'
    print('---------------------------')
    print(f'Loading Bill no. b{id}')
    for i in range(3):
        print(star)
        star += star
        time.sleep(0.8)
    print('---------------------------')
    c = crud.CRUD()
    c.printBill(id)


def printDoctor(did):
    did = f'd{did}'
    star = '*'
    print('---------------------------')
    print(f'Loading Physician ID: {did}')
    for i in range(3):
        print(star)
        star += star
        time.sleep(0.8)
    print('---------------------------')
    c = crud.CRUD()
    c.printDoctor(did)


def printList(pageNum, dataType):
    c = crud.CRUD()
    if dataType == 'p':
        c.listPatients(pageNum)
    elif dataType == 'd':
        c.listDoctors(pageNum)


def listMenu(dataType):
    exit = False
    pageNum = 1  # default to 1st page in list
    while exit is not True:
        print('----------------------------------------------------------------------')
        printList(pageNum, dataType)
        # print('Enter ')
        print('------------')
        print('Enter following for options(type \'exit\' in any input to move back to main menu):')
        if dataType == 'p':
            print('Enter 1 to print bill of patient')
        else:
            print('Enter 1 to view Physician details')
        print('Enter 2 to view more pages')
        print('Enter 3 to move back to main menu')
        print('------------')
        v = str(input('Enter option: ')).lower()
        if v == '1' and dataType == 'p':
            bill = False
            while bill is not True:
                b = str(input(
                    'Enter ID to view bill and Patient\' details: ')).lower()
                if b != 'exit':
                    try:
                        billID = int(b)
                        bill = True
                        printBill(billID)
                        print('----------------------------------------')
                        a = str(input('Continue to Patient\'s list menu?(y/n): '))
                        if a == 'y':
                            bill = True
                        elif a == 'n' or a == 'exit':
                            bill = True
                            exit = True
                            mainMenu()
                    except ValueError as e:
                        print('------------------------------------------------------')
                        print('Error! Invalid value for bill.')
                        print('------------------------------------------------------')
                elif b == 'exit':
                    bill = True
                    exit = True
                    mainMenu()
                else:
                    print('------------------------------------------------------')
                    print('Error! Invalid value entered')
                    print('------------------------------------------------------')

        elif v == '1' and dataType == 'd':
            dr = False
            while dr is not True:
                v = str(input('Enter the ID to view Doctor\'s details: '))
                try:
                    v = int(v)
                    printDoctor(v)
                    print('----------------------------------------')
                    a = str(input('Continue to Doctor\'s list menu?(y/n): '))
                    if a == 'y':
                        dr = True
                    elif a == 'n' or a == 'exit':
                        dr = True
                        exit = True
                        mainMenu()
                except ValueError as e:
                    print('------------------------------------------------------')
                    print('Error! Invalid value entered')
                    print('------------------------------------------------------')

        elif v == '2':
            pageNum = input('Enter Page No.').lower()
            if pageNum == 'exit':
                exit = True
                mainMenu()
            else:
                try:
                    pageNum = int(pageNum)
                except ValueError as e:
                    print('------------------------------------------------------')
                    print(f'Error! InValid value entered:\'{pageNum}\' . Defaulting to page 1')
                    print('------------------------------------------------------')
                    pageNum = 1
        elif v == '3':
            exit = True
            mainMenu()

        elif v == 'exit':
            exit = True
            mainMenu()

        else:
            print('------------------------------------------------------')
            print('Error! Invalid value entered')
            print('------------------------------------------------------')


def main(): mainMenu()

if __name__ == '__main__':
    main()
