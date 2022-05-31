import cmd
import person
import csvReaderWriter
import treatment
import listHelper


class Doctor(person.Person):
    def __init__(self):
        person.Person.__init__(self)
        self.__did = 'did'
        self.__tid = 'tid'
        self.__physician = 'physician'
        self.__csvHeader = [self.__did, self.__tid, self.__physician]
        self.__csvRow = {
            self.__did: '',
            self.__tid: '',
            self.__physician: ''

        }
        self.__csv = csvReaderWriter.CSVReaderWriter()
        self.__treatment = treatment.Treatment()
        self.__doctorData = self.__csv.reader('doctor.csv')
        self.__docList = []
    # using function from parent class with additional functionality
    def setID(self, idType):
        super().setID(idType)
        self.__csvRow[self.__did] = super().getID()

    # def setFirstName(self, fName):
    #     return super().setFirstName(fName)

    # def setLastName(self, lName):
    #     return super().setLastName(lName)

    # def setGender(self, gender):
    #     return super().setGender(gender)

    def setPhysicianType(self, tid):
        self.__treatment.setTreatmentDict(tid)
        self.__csvRow[self.__physician] = self.__treatment.getPhysician()
        self.__csvRow[self.__tid] = tid
        self.__treatment.reset()

    def setDoctorDict(self, did):
        if self.__doctorData == None:
            return False

        for i in self.__doctorData:
            if i[self.__did] == did:
                super().setPersonDict(did)
                self.__csvRow[self.__did] = i[self.__did]
                self.__csvRow[self.__tid] = i[self.__tid]
                self.__csvRow[self.__physician] = i[self.__physician]


    def getID(self):
        return super().getID()

    def getTID(self):
        return self.__csvRow[self.__tid]

    # def getFirstName(self):
    #     return super().getFirstName()

    # def getLastName(self):
    #     return super().getLastName()

    # def getGender(self):
    #     return super().getGender()

    def getPhysicianType(self):
        return self.__csvRow[self.__physician]

    def printSelectDoctor(self, tid):
        cli = cmd.Cmd()
        docListTemp = []
        docListFinal = []
        self.__docList = []
        for d in self.__doctorData:
            if d[self.__tid] == tid: # filter through doc list for only physicians for specific treatment
                docListTemp.append(d)
        for i in docListTemp:
            self.__docList.append(i[self.__did])
            a = f'ID:{i[self.__did]} -> {super().getFullName(i[self.__did])}' # find the doc names from person class
            docListFinal.append(a)
        str(docListFinal)
        # use CMD's column to print the list in less cluttered way
        cli.columnize(docListFinal, displaywidth=120)


    def doctorList(self, pageNum):
        newList = listHelper.ListHelper(self.__doctorData, pageNum, self.__did, super().getFullName)
        newList.setTotalNum()
        newList.setMaxNum()
        newList.setPages()
        newList.setFinalList()

        return [newList.getMaxNum(), newList.getTotalPages(), newList.getFinalList()]
        
    def verify(self, did):
        if not self.__docList:
            return False
        verified = False
        for i in self.__docList:
            if i == did:
                return True
            else:
                verified = False
        return verified

    def reset(self):
        self.__csvRow = {
            self.__did: '',
            self.__tid: '',
            self.__physician: ''
        }
    
    def writeNameToCsv(self):
        super().writeNameToCsv()
        self.__csv.writer('doctor.csv', self.__csvRow, self.__csvHeader)

