 # DoorCeptionist Start File
 # Author: Samuel Hinshelwood
 #
 # This file describes operational code for the DoorCeptionist Door Assistant
 # device. 
 #

from subprocess import call
from Scripts import Credentials
from Scripts import SpeechToText
from Scripts import SendEmail

RECORD_TIME = "10"

if __name__ == '__main__':

	# designate audio file
 	audioFilePath = Credentials.AUDIO_FILE_PATH

	# record audio/speech file from user
	call(["arecord", "-d", RECORD_TIME, "-f", "dat", "-t", "wav",
	      "D", "sysdefault:CARD=1", audioFilePath])

 	# capture its text
 	text = SpeechToText.recognize(audioFilePath)

 	# send an email containing audiofile and recognizable text
 	subject = "DoorCeptionist Doormail Alert"
 	body = 'This message was sent from your DoorCeptionist Device in ' + Credentials.LOCATION + "\n" \
	       'Please see the attached message from your guest: \n\n\"' + text + '\"'
	fileNamePlaceholder = "Visitor Message.wav"


 	SendEmail.sendWithAttachment(subject, body, fileNamePlaceholder, audioFilePath)

 	print "Message emailed successfully!"