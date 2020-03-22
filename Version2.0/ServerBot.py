import Message
from datetime import datetime
import time

messageObject = Message.SendMessage()
bcrecObject = Message.Bcrec()
chatID = -1001287723688

bcrecObject.getInitialBcrecNotice(10)
text = messageObject.createMessageWithDate("BCREC Notice Bot is ON")
messageObject.sendMessage(chatID,text)
while True:
    bcrecObject.getCurrentBcrecNotice(9)
    newNoticeFileName = bcrecObject.compaireNoticeFileNames()
    if newNoticeFileName:
        for fileNames in newNoticeFileName:
            messageObject.sendMessage(messageObject.createLink(fileNames))
        messageObject.sendMessage(messageObject.createMessageWithDate("Added on"))
        bcrecObject.getInitialBcrecNotice()

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



