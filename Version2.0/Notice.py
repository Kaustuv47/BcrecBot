import requests
from bs4 import BeautifulSoup

class Notice():
    def getInitialNotices(self,limit,webPageUrl):
        return self.fetchNoticeFileNames(limit,webPageUrl)

    def getCurrentNotices(self,limit,webPageUrl):
        return self.fetchNoticeFileNames(limit,webPageUrl)

    def fetchNoticeFileNames(self,limit,webPageUrl):
        noticeFileName = []
        serverResponse = requests.get(webPageUrl)
        soup = BeautifulSoup(serverResponse.text, "html.parser")
        for fileName in soup.findAll('a'):
            store = str(fileName.get('href'))
            if store.endswith('.pdf') and limit > 0:
                noticeFileName.append(store)
                limit=limit-1
        return noticeFileName

    def compaireNoticeFileNames(self, initialNoticeFileName, currentNoticeFileName):
        newNoticeFileNames = []
        for fileNames in currentNoticeFileName:
            if  fileNames not in initialNoticeFileName:
                newNoticeFileNames.append(fileNames)
        return newNoticeFileNames


