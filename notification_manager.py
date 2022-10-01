import os
from twilio.rest import Client

TWILIO_ACC_SID = "ACccc8c3e64e70c50ed7e16f08faabd5cf"
TWILIO_AUTH_TOKEN = "8292a4eb0c0467011c866d8b7f372c06"
MY_TWILIO_NO = "+19592712358"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_notification(self, info):
        account_sid = os.environ[TWILIO_ACC_SID]
        auth_token = os.environ[TWILIO_AUTH_TOKEN]
        client = Client(account_sid, auth_token)

        message = client.messages.create(body=info, from_=MY_TWILIO_NO, to="+2348101535488")
        print(message.sid)
