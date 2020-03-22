import datetime
import requests
import xlrd
from bs4 import BeautifulSoup
from Initializer import Initialize

class LoadLatestData(Initialize):
    noticeFile = []
    storedFile = []
    newFileNames = []
    def getLatestData(self):
        serverResponse = requests.get("http://bcrec.ac.in/noticeboard.htm")
        soup = BeautifulSoup(serverResponse.text, "html.parser")
        i = 0

        redundantFiles = ['netbanking.pdf', 'publication.pdf', 'Current_openings.pdf', 'free_seats.pdf']
        for fileName in soup.find_all('a'):
            if i <= 10 and fileName not in redundantFiles:
                store = str(fileName.get('href'))
                self.noticeFile.append(store)
                i = i+1
            else:
                break
        self.storedFile = self.makeListFile()
        self.noticeFile.reverse()
        for fileName in self.noticeFile:
            if fileName not in self.storedFile:
                self.writeFile(self.maxRows()+1,0,fileName)
                self.newFileNames.append(fileName)
        return self.newFileNames


class SendMessage:
    def __init__(self):
        self.token = "1077745875:AAERrzlD1O9jPSwg40RHZLDuv9IoirX0DeA"
        self.base = "https://api.telegram.org/bot{}/".format(self.token)

    def createLink(self, filename):
        store = "http://bcrec.ac.in/"+filename
        return store

    def createDate(self):
        date = datetime.datetime.now()
        date = date.strftime("%a, %b %d, %Y")
        return date

    def sendMessage(self, message):
        url = self.base + "sendMessage?chat_id={}&text={}".format("-449497571", message)
        if message is not None:
            requests.get(url)
