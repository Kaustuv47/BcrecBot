import requests
import datetime
from bs4 import BeautifulSoup


class Bcrec():
    initialNoticeFileName = []
    currentNoticeFileName = []
    def getInitialBcrecNotice(self,limit):
        self.initialNoticeFileName = self.fetchBcrecNoticeFileNames(limit)

    def getCurrentBcrecNotice(self,limit):
        self.currentNoticeFileName = self.fetchBcrecNoticeFileNames(limit)

    def fetchBcrecNoticeFileNames(self,limit):
        noticeFileName = []
        serverResponse = requests.get("http://bcrec.ac.in/noticeboard.htm")
        soup = BeautifulSoup(serverResponse.text, "html.parser")
        for fileName in soup.findAll('a'):
            store = str(fileName.get('href'))
            if store.endswith('.pdf') and limit > 0:
                noticeFileName.append(store)
                limit=limit-1
        return noticeFileName

    def compaireNoticeFileNames(self):
        newNoticeFileNames = []
        for fileNames in self.currentNoticeFileName:
            if  fileNames not in self.initialNoticeFileName:
                newNoticeFileNames.append(fileNames)
        return newNoticeFileNames


class SendMessage:
    def __init__(self):
        self.token = "TokenofChatBot"
        self.base = "https://api.telegram.org/bot{}/".format(self.token)

    def createLink(self, filename):
        return "http://bcrec.ac.in/"+filename

    def createMessageWithDate(self,message):
        date = datetime.datetime.now()
        return message+"\n"+date.strftime("%a, %b %d, %Y")

    def sendMessage(self,chatID, message):
        url = self.base + "sendMessage?chat_id={}&text={}".format(chatID, message)
        if message is not None:
            requests.get(url)
