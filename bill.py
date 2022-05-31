import csvReaderWriter
import treatment


class Bill:
    def __init__(self):
        self.__meds = 30
        self.__roomRent = 150
        self.__bid = 'bid'
        self.__pid = 'pid'
        self.__tid = 'tid'
        self.__medicine = 'medicine'
        self.__room = 'room'
        self.__dr = 'dr'
        self.__maxID = None
        self.__csvHeader = [self.__bid, self.__pid, self.__tid, 
                            self.__medicine, self.__room, self.__dr]
        self.__csvRow = {
            self.__bid: '',
            self.__pid: '',
            self.__tid: '',
            self.__medicine: '',
            self.__room: '',
            self.__dr: ''
        }
        self.__csv = csvReaderWriter.CSVReaderWriter()
        self.__billData = self.__csv.reader('bill.csv')
        self.__treatment = treatment.Treatment()

    def setID(self, id):
        bid = f'b{id}' # convert the pid to bXX ID
        self.__csvRow[self.__bid] = bid

    def setMaxID(self):
        billList = []
        for i in self.__billData:
            billList.append(int(i[self.__bid][1:]))
        self.__maxID = max(billList)

    def setPatientID(self, pid):
        self.__csvRow[self.__pid] = pid

    def setTreatmentID(self, tid):
        self.__csvRow[self.__tid] = tid

    def setMedicine(self, meds, days):
        if meds == None:
            self.__csvRow[self.__medicine] = self.__meds * days
        else:
            self.__csvRow[self.__medicine] = meds * days

    def setRoom(self, room, days):
        if room == None:
            self.__csvRow[self.__room] = self.__roomRent * days
        else:
            self.__csvRow[self.__room] = room * days

    def setDrFee(self, dr, tid):
        if dr == None:
            isCostly = self.__treatment.isCostly(tid)
            if isCostly:
                self.__csvRow[self.__dr] = 400
            else:
                self.__csvRow[self.__dr] = 250
        else:
            self.__csvRow[self.__dr] = dr

    def setBillDict(self, id):
        if self.__billData == None:
            return
        # convert the id to proper bXX ID in case the user enters an pXX ID
        bid = f'b{id[1:]}'
        for i in self.__billData:
            if i[self.__bid] == bid:
                self.__csvRow[self.__bid] = i[self.__bid]
                self.__csvRow[self.__pid] = i[self.__pid]
                self.__csvRow[self.__medicine] = i[self.__medicine]
                self.__csvRow[self.__room] = i[self.__room]
                self.__csvRow[self.__dr] = i[self.__dr]

    def getID(self):
        return self.__csvRow[self.__bid]

    def getMaxID(self):
        return self.__maxID

    def getPatientID(self):
        return self.__csvRow[self.__pid]

    def getMedicine(self):
        return self.__csvRow[self.__medicine]

    def getRoom(self):
        return self.__csvRow[self.__room]

    def getDrFee(self):
        return self.__csvRow[self.__dr]

    def verify(self, bid):
        billList = []
        maxNum = []
        for i in self.__billData:
            billList.append(i[self.__bid][1:])

        maxNum = max(billList)


    def sum(self):
        return float(self.__csvRow[self.__medicine]) + float(self.__csvRow[self.__room]) + float(self.__csvRow[self.__dr])

    def reset(self):
        self.__csvRow = {
            self.__bid: '',
            self.__pid: '',
            self.__medicine: '',
            self.__room: '',
            self.__dr: ''
        }
    
    def writeNameToCsv(self):
        self.__csv.writer('bill.csv', self.__csvRow, self.__csvHeader)
