import Message
import Notice
from datetime import datetime
import time

initialNoticeFileNameDict = {}

messageObject = Message.SendMessage()
noticeObject = Notice.Notice()

# Change need to be done in chatID
chatID = "Chat Id of person or Group"

# Ignore these Comments
  # 0 for Notice Board Url
  # 1 for Notice Starting Url

# Change need to be done in noticeBoardUrlDict
noticeBoardUrlDict = {"Name of institute":["Notice board Url","Starting URL of notices"],
                      "MAKAUT":["http://makautexam.net/announcement.html","http://makautexam.net/"]}


for key in noticeBoardUrlDict:
    initialNoticeFileNameDict[key] = noticeObject.getInitialNotices(10,noticeBoardUrlDict.get(key)[0])


text = messageObject.createMessageWithDate("Notice Bot for Institute Name is Active from \n")
messageObject.sendMessage(chatID,text)

while True:
    for key in noticeBoardUrlDict:
        # address = Notice board url
        address = noticeBoardUrlDict.get(key)[0]
        currentNoticeFileNameList = noticeObject.getCurrentNotices(9,address)
        newNoticeFileName = noticeObject.compaireNoticeFileNames(initialNoticeFileNameDict.get(key),currentNoticeFileNameList)

        if newNoticeFileName:
            for fileNames in newNoticeFileName:
                fileLink = messageObject.createLink(noticeBoardUrlDict.get(key)[1], fileNames)
                finalmessage = messageObject.createMessageWithDate(fileLink+"\n"+"From "+key+" ")
                messageObject.sendMessage(chatID, finalmessage)
            initialNoticeFileNameDict[key] = noticeObject.getInitialNotices(10,noticeBoardUrlDict.get(key)[0])

    currentTimeStamp = datetime.now()
    year = currentTimeStamp.year
    month = currentTimeStamp.month
    day = currentTimeStamp.day

    time00 = datetime(year,month,day,1)
    time21 = datetime(year,month,day,21)
    if currentTimeStamp > datetime(year,month,day,0) and currentTimeStamp < datetime(year,month,day,1):
        time.sleep(21600)
    else:
        time.sleep(600)


