 # DoorCeptionist Start File
 # Author: Samuel Hinshelwood
 #
 # This file describes operational code for the DoorCeptionist Door Assistant
 # device. 
 #

from Scripts import Credentials
from Scripts import SpeechToText
from Scripts import SendEmail

if __name__ == '__main__':

 	# collect the speech file
 	audioFilePath = Credentials.AUDIO_FILE_PATH

 	# capture its text
 	text = SpeechToText.recognize(audioFilePath)

 	# send an email containing audiofile and recognizable text
 	subject = "DoorCeptionist Doormail Alert"
 	body = 'This message was sent from your DoorCeptionist Device in ' + Credentials.LOCATION + "\n" \
	       'Please see the attached message from your guest: \n\n\"' + text + '\"'
	fileNamePlaceholder = "Visitor Message.wav"


 	SendEmail.sendWithAttachment(subject, body, fileNamePlaceholder, audioFilePath)

 	print "Message emailed successfully!"