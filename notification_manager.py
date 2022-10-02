from twilio.rest import Client

TWILIO_SID = "ACccc8c3e64e70c50ed7e16f08faabd5cf"
TWILIO_AUTH_TOKEN = "8292a4eb0c0467011c866d8b7f372c06"
TWILIO_VIRTUAL_NUMBER = "+19592712358"
TWILIO_VERIFIED_NUMBER = "+2348101535488"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
