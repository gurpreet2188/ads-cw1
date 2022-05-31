import csvReaderWriter

class Person:
    def __init__(self):
        self.__id = 'id' # key for the header
        self.__first_name = 'first_name' # key for the header
        self.__last_name = 'last_name' # key for the header
        self.__gender = 'gender' # key for the header
        self.__csvHeader = [self.__id, self.__first_name,
                         self.__last_name, self.__gender]  # Header for csv file
        self.__csvRow = {
            self.__id: '',
            self.__first_name: '',
            self.__last_name: '',
            self.__gender: '',
        }     #row for the csv file
        self.__csv = csvReaderWriter.CSVReaderWriter()
        self.__personData = self.__csv.reader('person.csv')


    def setID(self, idType):
        
        temp = []
        maxID = 0

        if self.__personData == None:  # check if csv is loaded
            return False

        if self.__csvRow[self.__id] != '':  # check if id exists or not
            return False
        
        for i in self.__personData:
            if idType == 'p':  # check idType: Patient or Doctor
                if i['id'][0] == 'p':  # find patient id in list
                    # this will get the numbers after the frist letter
                    temp.append(int(i['id'][1:]))
                    maxID = max(temp)
                    self.__csvRow[self.__id] = f'p{maxID + 1}'  # set the id
            elif idType == 'd':  # check idType: Patient or Doctor
                if i['id'][0] == 'd':  # find patient id in list
                    # this will get the numbers after the frist letter
                    temp.append(int(i['id'][1:]))
                    maxID = max(temp)
                    self.__csvRow[self.__id] = f'd{maxID + 1}'  # set the id

    def setFirstName(self, fName):
        self.__csvRow[self.__first_name] = fName

    def setLastName(self, lName):
        self.__csvRow[self.__last_name] = lName

    def setGender(self, gender):
        self.__csvRow[self.__gender] = gender

    def getID(self):
        return self.__csvRow[self.__id]

    def getFirstName(self):
        return self.__csvRow[self.__first_name]

    def getLastName(self):
        return self.__csvRow[self.__last_name]

    def getGender(self):
        return self.__csvRow[self.__gender]
    
    def setPersonDict(self, id):
        if self.__personData == None:  # check if csv is loaded
            return False
        
        for i in self.__personData:
            if i[self.__id] == id:
                self.__csvRow[self.__id] = i[self.__id]
                self.__csvRow[self.__first_name] = i[self.__first_name]
                self.__csvRow[self.__last_name] = i[self.__last_name]
                self.__csvRow[self.__gender] = i[self.__gender]

    def getFullName(self, id):
        if self.__personData:
            for i in self.__personData:
                if i['id'] == id:
                    return f'{i[self.__csvHeader[1]]} {i[self.__csvHeader[2]]}'


    def writeNameToCsv(self):
        self.__csv.writer('person.csv', self.__csvRow, self.__csvHeader)

    def reset(self):  # reset variables
        self.__csvRow = {
            self.__id: '',
            self.__first_name: '',
            self.__last_name: '',
            self.__gender: '',
        }
