from twilio.rest import TwilioRestClient

class SMS:
    def __init__(self, text_message):
        self.text_message = text_message

    # add phone number parameter
    def send_text(self):
        # print phone_number
        account_sid = ""
        auth_token = ""
        fromnumber = "+12248033227"
        tonumber = "+17733296548"
        client = TwilioRestClient(account_sid, auth_token)
        message = client.messages.create(
        to="+17733296548",
        from_="+12248033227",
        body=self.text_message)
        # return "Message successfully sent!"

new_sms = SMS("this is a text message")
new_sms.send_text()
