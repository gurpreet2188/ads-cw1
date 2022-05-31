import listHelper
import person, csvReaderWriter


class Patient(person.Person):
    def __init__(self):
        self.__pid = 'pid'
        self.__did = 'did'
        self.__tid = 'tid'
        self.__contact = 'contact'
        self.__address = 'address'
        self.__csvHeader = [self.__pid, self.__did,
                            self.__tid, self.__contact, self.__address]
        self.__csvRow = {
            self.__pid: '',
            self.__did: '',
            self.__tid: '',
            self.__contact: '',
            self.__address: ''
        }
        person.Person.__init__(self)
        self.__csv = csvReaderWriter.CSVReaderWriter()  # instance of csv Class
        self.__patientData = self.__csv.reader('patient.csv')

# using function from parent class with additional functionality
    def setID(self, idType):
        super().setID(idType)
        self.__csvRow[self.__pid] = super().getID()

    def setContact(self, contact):
        self.__csvRow[self.__contact] = contact

    def setAddress(self, address):
        self.__csvRow[self.__address] = address

    def setTreatment(self, tid):
        self.__csvRow[self.__tid] = tid

    def setDoctorID(self, did):
        self.__csvRow[self.__did] = did

    def setPatientDict(self, pid):
        if self.__patientData == None:
            return False

        for i in self.__patientData:
            if i[self.__pid] == pid:
                super().setPersonDict(pid)
                self.__csvRow[self.__pid] = i[self.__pid]
                self.__csvRow[self.__did] = i[self.__did]
                self.__csvRow[self.__tid] = i[self.__tid]
                self.__csvRow[self.__contact] = i[self.__contact]
                self.__csvRow[self.__address] = i[self.__address]

    def getID(self):
        return self.__csvRow[self.__pid]

    def getContact(self):
        return self.__csvRow[self.__contact]

    def getAddress(self):
        return self.__csvRow[self.__address]

    def getTreatment(self):
        return self.__csvRow[self.__tid]

    def getDoctorID(self):
        return self.__csvRow[self.__did]

    def patientList(self, pageNum):
        newList = listHelper.ListHelper(self.__patientData, pageNum, self.__pid, super().getFullName)
        newList.setTotalNum()
        newList.setMaxNum()
        newList.setPages()
        newList.setFinalList()

        return [newList.getMaxNum(), newList.getTotalPages(), newList.getFinalList()]

    def writeNameToCsv(self):
        super().writeNameToCsv()
        self.__csv.writer('patient.csv', self.__csvRow, self.__csvHeader)
