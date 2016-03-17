# SendEmails.py
# This file describes functions for sending emails programmatically.  

import smtplib #standard email module
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
import Credentials

# Message Send Config

FROM = Credentials.FROM
TO = [Credentials.TO] # must be a list
TO = ", ".join(TO)

SUBJECT = "DoorCeptionist Doormail Alert"

BODY = "This message was sent from your DoorCeptionist Device in " + Credentials.LOCATION + "\n" \
	   "Please see the attached message from your guest: "

FILENAME = "Visitor Message.wav" # for email name scheme
ATTACHMENT = open("/Users/samuelhinshelwood/Downloads/foobar.wav", "rb") # for finding file on computer

# Prepare email config & body

message = MIMEMultipart()
message['From'] = FROM
message['To'] = TO
message['Subject'] = SUBJECT
message.attach(MIMEText(BODY, 'plain'))

# prepare email attachment (encoding)

part = MIMEBase('application', 'octet-stream')
part.set_payload((ATTACHMENT).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % FILENAME)
message.attach(part)

# Login to email server

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(Credentials.USERNAME, Credentials.PASSWORD)

messageText = message.as_string()

# Send the email

server.sendmail(FROM, TO, messageText)
server.quit()