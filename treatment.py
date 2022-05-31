import cmd
import csvReaderWriter


class Treatment():
    def __init__(self):
        self.__tid = 'tid'
        self.__treatment = 'treatment'
        self.__physician = 'physician'
        self.__csvHeader = [self.__tid, self.__treatment, self.__physician]
        self.__csvRow = {
            self.__tid: '',
            self.__treatment: '',
            self.__physician: ''

        }
        self.__treatmentList = []
        self.__csv = csvReaderWriter.CSVReaderWriter()
        self.__treatmentData = self.__csv.reader('treatments.csv')

    # def setID(self):
    #     pass

    # def setTreatment(self):
    #     pass

    # def setPhysician(self):
    #     pass

    def setTreatmentDict(self, tid):
        if self.__treatmentData == None:
            return False

        for i in self.__treatmentData:
            if i[self.__tid] == tid:
                self.__csvRow[self.__tid] = i[self.__tid]
                self.__csvRow[self.__treatment] = i[self.__treatment]
                self.__csvRow[self.__physician] = i[self.__physician]

    def getID(self):
        return self.__csvRow[self.__tid]

    def getTreatment(self):
        return self.__csvRow[self.__treatment]

    def getPhysician(self):
        return self.__csvRow[self.__physician]

    def printTreatments(self):
        Treatment.__printList(self, self.__treatment)

    def printPhysicianType(self):
        Treatment.__printList(self, self.__physician)

    def __printList(self, idType):
        cli = cmd.Cmd()
        l = []
        if self.__treatmentData == None:
            return False

        self.__treatmentList= [] # reset if any data exist
        for i in self.__treatmentData:
            self.__treatmentList.append(i[self.__tid])
            p = f'ID: {i[self.__tid]} -> {i[idType]}'
            l.append(p)

        str(l)
        cli.columnize(l, displaywidth=120)
        
    def verify(self, tid):
        if self.__treatmentList == []:
            return False
        verified = False
        for i in self.__treatmentList:
            if i == tid:
                return True
            else:
                verified = False
        return verified
    
    def isCostly(self, tid):
         if tid == 't4' or tid == 't7' or tid == 't8':
            return True
         else: 
            return False          

    def reset(self):
        self.__csvRow = {
            self.__tid: '',
            self.__treatment: '',
            self.__physician: ''
        }
