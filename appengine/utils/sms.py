from twilio.rest import Client

class SMS:
    def __init__(self, text_message):
        self.text_message = text_message

    def send_text(self, contact):
        account_sid = "test-sid"
        auth_token = "test-token"
        fromnumber = "+12248033227"
        tonumber = contact,
        client = Client(account_sid, auth_token)
        message = client.messages.create(
        to="+17733296548",
        from_="+12248033227",
        body=self.text_message)
