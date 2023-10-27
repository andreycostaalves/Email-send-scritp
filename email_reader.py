from imbox import Imbox
from datetime import datetime
import pandas as pd

username = 'seuemail@gmail.com'
password = open('pass', 'r').read()
host = 'imap.gmail.com' #o servidor do provedor de email esse caso é o do gmail.com

mail = Imbox(host, username=username, password=password, ssl=True)
messages = mail.messages(unread=True)
len(messages)

for (uid, message) in messages:
    message.subject
    message.body
    message.sent_from
    message.sent_to
    message.cc
    message.headers
    message.date

    if len(message.attachments) > 0:
        for attach in message.attachments:
            file = open('attachments/report.pdf', 'wb')
            attach['content'].seek(0)
            file.write(attach['content'].read())
            file.close()
