from datetime import date, datetime
import csvReaderWriter


class Date:
    def __init__(self):
        self.__pid = 'pid'
        self.__dob = 'dob'
        self.__admitted = 'admitted'
        self.__discharged = 'discharged'
        self.__csv = csvReaderWriter.CSVReaderWriter()
        self.__dateData = self.__csv.reader('dates.csv')
        self.__csvHeader = [self.__pid, self.__dob,
                            self.__admitted, self.__discharged]
        self.__csvRow = {
            self.__pid: '',
            self.__dob: '',
            self.__admitted: '',
            self.__discharged: '',
        }

    def setID(self, pid):
        self.__csvRow[self.__pid] = pid

    def setDOB(self, dob):
        self.__csvRow[self.__dob] = Date.__setDateFormat(self, dob)

    def setAdmitted(self, admitted):
        self.__csvRow[self.__admitted] = Date.__setDateFormat(self, admitted)

    def setDischarged(self, discharged):
        self.__csvRow[self.__discharged] = Date.__setDateFormat(self, discharged)

    def setDateDict(self, pid):
        if self.__dateData:
            for i in self.__dateData:
                if i[self.__pid] == pid:
                    self.__csvRow[self.__pid] = i[self.__pid]
                    self.__csvRow[self.__dob] = i[self.__dob]
                    self.__csvRow[self.__admitted] = i[self.__admitted]
                    self.__csvRow[self.__discharged] = i[self.__discharged]

    def getID(self):
        return self.__csvRow[self.__pid]

    def getDOB(self):
        return self.__csvRow[self.__dob]

    def getAdmitted(self):
        return self.__csvRow[self.__admitted]

    def getDischarged(self):
        return self.__csvRow[self.__discharged]

    def getAge(self):
        return Date.calculateDelta(self, 'age', Date.getDOB(self), None)

    def getDays(self):
        return Date.calculateDelta(self, 'day', Date.getAdmitted(self), Date.getDischarged(self))

    def __setDateFormat(self, date):
        oldDate = ''
        newDate = ''
        for i in ('%d-%m-%Y', '%d/%m/%Y', '%d.%m.%Y'):
            try:
                oldDate = datetime.strptime(str(date), i)
            except ValueError:
                pass

        newDate = datetime.strftime(oldDate, '%d-%m-%Y')
        return newDate

    def verifyDateFormat(self, d):
        if date:
            for i in ('%d-%m-%Y', '%d/%m/%Y', '%d.%m.%Y'):
                try:
                    datetime.strptime(d, i)
                    return True
                except ValueError:
                    pass
            return False

    def verifyAge(self, d):
        delta = Date.calculateDelta(self, 'age', d, date.today())
        if delta <= 16:
            return False
        else:
            return True

    def verifyDateDelta(self, start, end):
        delta = Date.calculateDelta(self, 'day', start, end)
        if delta <= 3:
            return False
        else:
            return True

    def calculateDelta(self, dateType, start, end):
        start = Date.__convertDate(self, start)
        if dateType == 'age':
            end = date.today()
            # dob(year) - current(year) - (if true : 1 false: 0)
            return end.year - start.year - ((end.month, end.day) < (start.month, start.day))
        elif dateType == 'day':
            end = Date.__convertDate(self, end)
            delta = date(end.year, end.month, end.day) - \
                    date(start.year, start.month, start.day)
            return delta.days

    def __convertDate(self, dateString):
        dateString = Date.__setDateFormat(self, dateString)
        return datetime.strptime(str(dateString), '%d-%m-%Y')

    def reset(self):
        self.__csvRow = {
            self.__pid: '',
            self.__dob: '',
            self.__admitted: '',
            self.__discharged: '',
        }

    def writeNameToCsv(self):
        self.__csv.writer('dates.csv', self.__csvRow, self.__csvHeader)
