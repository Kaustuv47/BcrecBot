import requests
import datetime

class SendMessage:
    def __init__(self):
        # Change need to be done in token id
        self.token = "Enter the Bot token ID"
        self.base = "https://api.telegram.org/bot{}/".format(self.token)

    def createLink(self, startingUrl, filename):
        return startingUrl+filename

    def createMessageWithDate(self,message):
        date = datetime.datetime.now()
        return message+date.strftime("%a, %b %d, %Y")

    def sendMessage(self,chatID, message):
        url = self.base + "sendMessage?chat_id={}&text={}".format(chatID, message)
        if message is not None:
            requests.get(url)
