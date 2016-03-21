# File describes functions for interfacing with IBM Speech to Text API
# using requests (Python HTTP Requests) library

import requests



# Return current IBM S2T transcription models
def getModels():
	# get HTTP response (a response code)
	# prints available IBM T2S Translation Models
	response = requests.get("https://watson-api-explorer.mybluemix.net/speech-to-text/api/v1/models")

	# convert to JSON format
	response = response.json()

	print response

# Transcribe audio file using S2T service
def recognize():
	# S2T Recognize Endpoint
	url = 'https://watson-api-explorer.mybluemix.net/speech-to-text/api/v1/recognize'

	# HTTP Request headers
	headers={'Content-Type': 'audio/wav'}

	# collect audio file to dictate
	audio = open('/Users/samuelhinshelwood/Downloads/foobar.wav', 'rb')

	# Send request, receive response from IBM server
	response = requests.post(url, headers=headers, data=audio)

	# Convert to JSON format
	response = response.json()

	# Parse IBM S2T response for transcription
	text = response[ 'results' ]
	text = text[0]
	text = text[ 'alternatives' ]
	text = text[0]
	text = text[ 'transcript' ]
	print("Text returned from IBM S2T Service: " + 
		text)


if __name__ == '__main__':
	recognize()

