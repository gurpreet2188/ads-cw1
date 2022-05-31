import cmd
import patient
import doctor
import treatment
import date
import bill


class CRUD:
    def __init__(self):
        self.__patient = patient.Patient()
        self.__treatment = treatment.Treatment()
        self.__doctor = doctor.Doctor()
        self.__date = date.Date()
        self.__bill = bill.Bill()
        self.__pid = ''
        self.__tid = ''
        self.__did = ''
        self.__dob = ''
        self.__doa = ''
        self.__dod = ''
        self.__days = 0

    def addPatient(self):
        p = self.__patient
        p.setID('p')
        self.__pid = p.getID()
        fName = str(input('Enter First Name: '))
        p.setFirstName(fName)
        lName = str(input('Enter Last Name: '))
        p.setLastName(lName)
        gender = str(input('Enter Gender: '))
        p.setGender(gender)
        contact = str(input('Enter Phone Number: '))
        p.setContact(contact)
        address = str(input('Enter Address: '))
        p.setAddress(address)

        # --set Dates
        CRUD.__setDates(self)

        # --set Treament Type
        CRUD.__setTreament(self)
        p.setTreatment(self.__tid)

        # --link with Physician ID and Type
        CRUD.__setDoctor(self)
        p.setDoctorID(self.__did)

        # --set bill
        CRUD.__setBill(self)

        # --print
        CRUD.___printConfirmation(self)

        # save and print the bill
        v = ''
        check = False
        while check is not True:
            v = str(input('Save Details and print bill?(y/n): '))
            if v == 'y':
                check = True
                CRUD.__saveDetails(self,'p')
                break
            elif v == 'n':
                check = True
                break

        return v  # return user's choice to move back to main menu

    def __setTreament(self):
        t = self.__treatment
        treatmentVerified = False
        while treatmentVerified is not True:
            print('')
            print('===========Treaments===============')
            t.printTreatments()
            print('===================================')
            self.__tid = str(input('Enter Treament ID from above List: '))
            treatmentVerified = t.verify(self.__tid)
            if treatmentVerified == False:
                print('')
                print('!!!!!!Error!!!!!!')
                print(
                    self.__tid, 'not found in below list, please check the ID and enter again.')
                print('=================')
                print('')
                
    def __setDoctor(self):
        dr = self.__doctor
        docVerified = False
        while docVerified is not True:
            print('')
            print('===========Doctors============')
            dr.printSelectDoctor(self.__tid)
            print('==============================')
            self.__did = str(input('Enter Doctor ID from above List: '))
            docVerified = dr.verify(self.__did)
            if docVerified is not True:
                print('')
                print('!!!!!!Error!!!!!!')
                print(
                    self.__did, 'not found in below list, please check the ID and enter again.')
                print('=================')

    def __setDates(self):
        d = self.__date

        d.setID(self.__pid)
        self.__dob = CRUD.__isValidAge(self, 'birth')
        d.setDOB(self.__dob)
        self.__doa = CRUD.__isValidDate(self, 'admission')
        d.setAdmitted(self.__doa)
        self.__dod = CRUD.__isvalidDelta(self, 'discharged')
        d.setDischarged(self.__dod)

    def __isValidAge(self, dateType):
        d = self.__date
        date = CRUD.__isValidDate(self, dateType)
        isValid = False
        while isValid is not True:
            # date = str(input(f'Enter Date of {dateType}(dd-mm-yyyy): '))
            isValid = d.verifyAge(date)
            if isValid is not True:
                print('')
                print('!!!!!!Error!!!!!!')
                print(
                    date, ' :patient below age 16 are not admitted in hospital as pediatricians are on Holiday')
                print('=================')
                date = str(input(f'Enter Date of {dateType}(dd-mm-yyyy): '))

        return date

    def __isvalidDelta(self, dateType):
        d = self.__date
        date = CRUD.__isValidDate(self, dateType)
        isValid = False
        while isValid is not True:
            # date = str(input(f'Enter Date of {dateType}(dd-mm-yyyy): '))
            isValid = d.verifyDateDelta(self.__doa, date)
            if isValid is not True:
                print('')
                print('!!!!!!Error!!!!!!')
                print(date, ' :patient is admitted for at least 3 days or more')
                print('=================')
                date = str(input(f'Enter Date of {dateType}(dd-mm-yyyy): '))
        self.__days = d.calculateDelta('day', self.__doa, date)
        return date

    def __isValidDate(self, dateType):
        d = self.__date
        date = ''
        isValid = False
        while isValid is not True:
            date = str(input(f'Enter Date of {dateType}(dd-mm-yyyy): '))
            isValid = d.verifyDateFormat(date)
            if isValid is not True:
                print('')
                print('!!!!!!Error!!!!!!')
                print(date, ' :not a valid date format')
                print('=================')
        return date

    def __setBill(self):
        b = self.__bill

        auto = str(input('Auto calculate the individual Rates ?(y/n): '))
        b.setID(CRUD.getID(self))
        b.setPatientID(self.__pid)
        print(b.getPatientID())
        b.setTreatmentID(self.__tid)
        if auto == 'y':
            b.setMedicine(None, self.__days)
            b.setRoom(None, self.__days)
            b.setDrFee(None, self.__tid)
        elif auto == 'n':
            m = False
            while m is not True:
                try:
                    a = float(input('Eneter charges for the Medicines: '))
                    b.setMedicine(a, self.__days)
                    m = True
                except ValueError as e:
                    print('Error! invalid value.')
            r = False
            while r is not True:
                try:
                    a = float(input('Eneter charges for the Room(per night): '))
                    b.setRoom(a, self.__days)
                    r = True
                except ValueError as e:
                    print('Error! invalid value.')
            d = False
            while d is not True:
                try:
                    a = float(input('Eneter charges for the Doctor Fee: '))
                    b.setDrFee(a, self.__tid)
                    d = True
                except ValueError as e:
                    print('Error! invalid value.')



    def ___printConfirmation(self):
        p = self.__patient
        dr = self.__doctor
        t = self.__treatment
        d = self.__date
        b = self.__bill
        print('= = = Details = = =')
        print('ID: ', p.getID())
        print('Name: ', p.getFirstName(), p.getLastName())
        print('Gender: ', p.getGender())
        print('Phone Numer: ', p.getContact())
        print('Address: ', p.getAddress())
        print('Attending Dr. ', dr.getFullName(self.__did))
        t.setTreatmentDict(self.__tid)
        print('Treatment: ', t.getTreatment())
        print('Date of Birth: ', d.getDOB())
        print('Date of Admission: ', d.getAdmitted())
        print('Date of Discharged: ', d.getDischarged())
        print('Medicine Charges: ', b.getMedicine())
        print('Room Rent: ', b.getRoom())
        print("Doctor's Fee: ", b.getDrFee())

    def addDoctor(self):
        dr = self.__doctor
        t = self.__treatment
        # add name
        # select treatment
        dr.setID('d')

        fName = str(input('Enter First Name: '))
        dr.setFirstName(fName)
        lName = str(input('Enter Last Name: '))
        dr.setLastName(lName)
        gender = str(input('Enter Gender: '))
        dr.setGender(gender)
        CRUD.__setTreament(self)
        dr.setPhysicianType(self.__tid)
        CRUD.__printConfirmationDoctor(self)
        # save and print the bill
        v = ''
        check = False
        while check is not True:
            v = str(input('Save Details?(y/n): '))
            if v == 'y':
                check = True
                dr.writeNameToCsv()
                break
            elif v == 'n':
                check = True
                break

        return v  # return user's choice to move back to main menu

    def __printConfirmationDoctor(self):
        dr = self.__doctor
        t = self.__treatment
        t.setTreatmentDict(self.__tid)
        print('')
        print('---------New Doctor Details---------------')
        print('Name Dr. ', dr.getFirstName(), dr.getLastName(), f'({t.getPhysician()})')
        print('Treatment: ', t.getTreatment())
        print('------------------------------------------')
        check = False
       

    def printBill(self, id):
        p = self.__patient
        dr = self.__doctor
        t = self.__treatment
        d = self.__date
        b = self.__bill
        b.setMaxID()
        if b.getMaxID() >= id >= 1:
            id = f'p{id}'
            p.setPatientDict(id)
            d.setDateDict(id)
            b.setBillDict(id)
        else:
            return print(f'Error! b{id} not found.')

        self.__pid = id
        self.__tid = p.getTreatment()
        self.__did = p.getDoctorID()

        print(f'= = = = = = Bill No.{b.getID()} = = = = = = = =')
        print('')
        print('= = = = = =  Patient\'s Info = = = = = =')
        print('ID: ', p.getID())
        print('Name: ', p.getFirstName(), p.getLastName())
        print('Gender: ', p.getGender())
        print('Date of Birth: ', d.getDOB())
        print('Age: ', d.getAge())
        print('Date of Admission: ', d.getAdmitted())
        print('Date of Discharged: ', d.getDischarged())
        print('Phone Numer: ', p.getContact())
        print('Address: ', p.getAddress())
        t.setTreatmentDict(self.__tid)
        print('Treatment: ', t.getTreatment())
        print('')
        print('= = = = = =  Physician Info = = = = = =')
        print(f'Attended by ({t.getPhysician()}) Dr.', dr.getFullName(self.__did))
        print('')
        print('= = = = = = = = Charges = = = = = = = =')
        print('Medicine: ', b.getMedicine())
        print(f'Room Rent for {d.getDays()} days: ', b.getRoom())
        print("Doctor's Fee: ", b.getDrFee())
        print('= = = = = = = Total = = = = = = = = = =')
        print('Total:                          ', b.sum())
        print('= = = = = = = = = = = = = = = = = = = =')

    # def updatePatient(self, id):
    #     p = self.__patient
    #     dr = self.__doctor
    #     t = self.__treatment
    #     d = self.__date
    #     b = self.__bill
    #
    #     p.setPatientDict(id)
    #     dr.setPersonDict(id)
    #     t.setTreatmentDict(id)
    #     d.setDateDict(id)
    #     b.setBillDict(id)
    #
    #     self.__pid = id
    #     self.__tid = p.getTreatment()
    #     self.__did = p.getDoctorID()
    #
    #

    def listPatients(self, pageNum):
        cli = cmd.Cmd()
        p = self.__patient
        cli.columnize(p.patientList(pageNum)[2], displaywidth=120)
        print('------------------------------------------------------')
        print(f'Showing page {pageNum} of {p.patientList(pageNum)[1]}')
        print('------------------------------------------------------')

    def listDoctors(self, pageNum):
        cli = cmd.Cmd()
        dr = self.__doctor
        cli.columnize(dr.doctorList(pageNum)[2], displaywidth=120)
        print('------------------------------------------------------')
        print(f'Showing page {pageNum} of {dr.doctorList(pageNum)[1]}')
        print('------------------------------------------------------')

    def printDoctor(self, did):
        dr = self.__doctor
        t = self.__treatment
        dr.setPersonDict(did)
        t.setTreatmentDict(dr.getTID())
        print(f'Name: Dr.{dr.getFirstName(), dr.getLastName()}({dr.getPhysicianType()})')
        print(f'Speciality: {t.getTreatment()}')
        print(f'Gender: {dr.getGender()}')
        dr.reset()
        t.reset()

    def __saveDetails(self, saveType):
        p = self.__patient
        dr = self.__doctor
        t = self.__treatment
        d = self.__date
        b = self.__bill

        if saveType == 'p':
            p.writeNameToCsv()
            d.writeNameToCsv()
            b.writeNameToCsv()

        elif saveType == 'dr':
            dr.writeNameToCsv()

    def getID(self):
        return int(self.__pid[1:]) # return the ID number only
