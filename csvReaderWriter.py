# A simple class to handle the reading and writing
# of the data from csv files.
import csv


class CSVReaderWriter:
    def __init__(self):
        pass  #

    # read from csv file and output the data in
    # Dictionary data type with csv's DictReader
    # Parameters: file -> name of the file to read
    # data from.
    def reader(self, file):
        temp = []
        with open(file, 'r') as f:
            r = csv.DictReader(f, delimiter=',')
            for i in r:
                temp.append(i)
        return temp

    # Return the date stored in variable from csv file
    # def getReaderData(self):
    #     return self.__readData

    # Append the data to csv files in same Dictionary
    # data type 
    # Parameters: file -> name of the file to append
    #             data to.
    #             row -> a single row of data in Dictionary
    #             data type.
    #             header -> header for the csv file.
    def writer(self, file, row, header):
        with open(file, 'a', newline='') as file:
            w = csv.DictWriter(file, header)
            w.writerow(row)

    def writerNew(self, file, row, header):
        with open(file, 'w', newline='') as file:
            w = csv.DictWriter(file, header)
            w.writeheader()
            w.writerows(row)
