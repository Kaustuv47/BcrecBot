from Initializer import Initialize
from SendMessage import SendMessage
from SendMessage import LoadLatestData
import time

init = Initialize()
message = SendMessage()
message.sendMessage("Hello this is Bcrec NoticeBoard")
# message.sendMessage("Notice Board Creation Successful")
# message.sendMessage("Downloading All links")
# batchMessage = init.batchMessage()
# for item in batchMessage:
#     link = SendMessage().createLink(item)
#     message.sendMessage(link)
loadLatest = LoadLatestData()
while True:
    newFileNames = loadLatest.getLatestData()
    if newFileNames != []:
        for item in newFileNames:
            print(item)
            link = message.createLink(item)+"\n"+message.createDate()
            print(link)
            #message.sendMessage(link)
    time.sleep(900)




