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

# Send email with desired attachment and additional text
# subject            - string email subject
# body               - string body of message
# attachmentName     - string desired name placeholder for attachment in email
# attachmentFilePath - path to the desired file
def sendWithAttachment(subject, body, attachmentName, attachmentFilePath):

	# Prepare email config & body

	message = MIMEMultipart()
	message['From'] = FROM
	message['To'] = TO
	message['subject'] = subject
	message.attach(MIMEText(body, 'plain'))


	# prepare email attachment (encoding)

	attachmentFile = open(attachmentFilePath, 'rb') # open file
	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachmentFile).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % attachmentName)
	message.attach(part)

	# Login to email server

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(Credentials.USERNAME, Credentials.PASSWORD)

	messageText = message.as_string()

	# Send the email

	server.sendmail(FROM, TO, messageText)
	server.quit()

	attachmentFile.close() # close file

#if __name__ == '__main__':
	# sendWithAttachment(open("/Users/samuelhinshelwood/Downloads/foobar.wav", "rb"), "")
	# print("Email has been sent to recipient %s!" % TO)