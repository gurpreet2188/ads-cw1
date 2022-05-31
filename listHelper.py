class ListHelper:
    def __init__(self, mainList, pageNum, idType, getName):  # set variables
        self.__mainList = mainList
        self.__pageNum = pageNum
        self.__idType = idType
        self.__getName = getName
        self.__allIDs = []
        self.__maxNum = 0
        self.__totalPages = 0
        self.__start = []
        self.__end = []
        self.__finalList = []

    def setTotalNum(self):
        for i in self.__mainList:
            num = int(i[self.__idType][1:]) # check if patient or doctor id 
            self.__allIDs.append(num) # append the respective IDs

    def setMaxNum(self):
        self.__maxNum = max(self.__allIDs) # get the max ID Number to be used for setting end index in list

    def setPages(self):
        for i in range(1, self.__maxNum, 20): # set 20 items per page by looping in steps of 20
            if i == 1:
                self.__start.append(0) # set the starting index for initial list 
            else:
                self.__start.append(i - 1) # set the starting index for the second to rest of the pages
                self.__end.append(i - 1) # set the ending index for initial and other pages
            self.__totalPages += 1 # set total number of pages 3

    def setFinalList(self):
        if 0 < self.__pageNum < self.__totalPages: # check page number entered by user
            # slice through patient or doctor list with starting and ending indexes
            for i in self.__mainList[self.__start[self.__pageNum - 1]:self.__end[self.__pageNum - 1]]: 
                # get the ID and name from person class with .__getName method 
                a = f'ID:{i[self.__idType][1:]} -> {self.__getName(i[self.__idType])}'
                self.__finalList.append(a) # append to final list

        elif self.__pageNum == self.__totalPages:# check page number entered by user == last page
             # slice through patient or doctor list with starting and setting ending index as Max number
            for i in self.__mainList[self.__start[self.__pageNum - 1]:self.__maxNum]:
                # get the ID and name from person class with .__getName method 
                a = f'ID:{i[self.__idType][1:]} -> {self.__getName(i[self.__idType])}'
                self.__finalList.append(a) # append to final list

        elif self.__pageNum > self.__totalPages:
            print('404 Page not found.') # return this if page number no found

    def getMaxNum(self):
        return self.__maxNum

    def getTotalPages(self):
        return self.__totalPages

    def getFinalList(self):
        return self.__finalList