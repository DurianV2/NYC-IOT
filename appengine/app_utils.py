from utils.sms import SMS

def send_second_level_sms(host, contacts):
    message_handler = SMS(host + " has not returned home")
    for contact in contacts:
        message_handler.send_text()

def send_third_level_sms(host):
    message_handler = SMS(host + " has not returned home! Please help")
    message_handler.send_text()


