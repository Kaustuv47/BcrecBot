import requests
import xlrd
import xlwt
from bs4 import BeautifulSoup
from xlrd import *
from xlutils.copy import copy



class Initialize():
    """docstring forBcrec Notice Board Chat Bot."""

    noticeFile = []

    def __init__(self):
        self.token = "1077745875:AAERrzlD1O9jPSwg40RHZLDuv9IoirX0DeA"
        self.base = "https://api.telegram.org/bot{}/".format(self.token)
        self.writeFile(0, 0, 0)
        self.getAllData()

    def getAllData(self):
        serverResponse = requests.get("http://bcrec.ac.in/noticeboard.htm")
        soup = BeautifulSoup(serverResponse.text, "html.parser")
        writeBook = copy(open_workbook('DataBase.xls'))

        for fileName in soup.findAll('a'):
            store = str(fileName.get('href'))
            if store.endswith('.pdf'):
                self.noticeFile.append(store)
        self.removeSomeFile()
        i = 0
        for fileName in self.noticeFile:
            writeBook.get_sheet(0).write(i, 0, fileName)
            i = i + 1
        writeBook.save('DataBase.xls')

    def writeFile(self, row, col, data):
        try:
            writeBook = copy(open_workbook('DataBase.xls'))
            writeBook.get_sheet(0).write(row, col, data)
            writeBook.save('DataBase.xls')
        except FileNotFoundError:
            writeBook = xlwt.Workbook('DataBase.xls')
            writeSheet = writeBook.add_sheet('Sheet', cell_overwrite_ok=True)
            writeBook.get_sheet(0).write(row, col, data)
            writeBook.save('DataBase.xls')

    def readFile(self, row, col):
        readBook = xlrd.open_workbook('DataBase.xls')
        readSheet = readBook.sheet_by_index(0)
        return readSheet.cell_value(row, col)
    def makeListFile(self):
        for i in range(self.maxRows()):
            self.noticeFile.append(self.readFile(i,0))
        return self.noticeFile

    def maxRows(self):
        readBook = xlrd.open_workbook('DataBase.xls')
        readSheet = readBook.sheet_by_index(0)
        return readSheet.nrows

    def removeSomeFile(self):
        try:
            self.noticeFile.remove('netbanking.pdf')
            self.noticeFile.remove('publication.pdf')
            self.noticeFile.remove('Current_openings.pdf')
            self.noticeFile.reverse()
            self.noticeFile.remove('free_seats.pdf')
            self.noticeFile.remove('netbanking.pdf')
            self.noticeFile.remove('publication.pdf')
            self.noticeFile.remove('Current_openings.pdf')
        except ValueError:
            print("Error")

    def batchMessage(self):
        return self.noticeFile

