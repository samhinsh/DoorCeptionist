# SendEmails.py
# This file describes functions for sending emails programmatically.  

import smtplib #standard email module

SERVER = "localhost"

FROM = "samhinsh@stanford.edu"
TO = ["samhinsh@stanford.edu"] # must be a list

SUBJECT = "DoorCeptionist Doormail Alert"

BODY = "This message was sent from your DoorCeptionist Device in Ujamaa 271." \
	   "Please see the attached message from your guest: "

# Prepare actual email

message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, BODY)

# Send the email

server = smtplib.SMTP(SERVER)
server.sendmail(FROM, TO, message)
server.quit()