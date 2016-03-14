# SendEmails.py
# This file describes functions for sending emails programmatically.  

import smtplib #standard email module
import Credentials

FROM = Credentials.FROM
TO = [Credentials.TO] # must be a list

SUBJECT = "DoorCeptionist Doormail Alert"

BODY = "This message was sent from your DoorCeptionist Device in " + Credentials.LOCATION + "\n" \
	   "Please see the attached message from your guest: "


# Login to email server

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(Credentials.USERNAME, Credentials.PASSWORD)

# Prepare actual email

message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, BODY)

# Send the email

server.sendmail(FROM, TO, message)
server.quit()