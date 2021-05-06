# This code to run in RPi at startup

import RPi.GPIO as GPIO
import os
import pyttsx3
import cv2 
import numpy as np
import pytesseract
from picamera.array import PiRGBArray
from picamera import PiCamera
from datetime import datetime
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# setting up shutter button on GPIO pin 5
GPIO.setmode(GPIO.BCM)
button=5
GPIO.setup(button,GPIO.IN)

# Azure storage account tokens
connect_str = '[REMOVED FOR PRIVACY]'

# setting up camera
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 90

# setting up TTS Engine
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', 'english+f1')

# initializing camera
rawCapture = PiRGBArray(camera, size=(640, 480))

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	image = frame.array
	cv2.imshow("Frame", image)
	rawCapture.truncate(0)
	text=''
	img=image

	# ocr
	original = pytesseract.image_to_string(img, config='-l eng --oem 3 --psm 12', nice=0)
	text = original
	print(text)
	
	# TTS
	engine.say(text)
	engine.runAndWait()

	# shutter button
	button_state=0
	button_state=GPIO.input(button)
	print(button_state)
	if button_state==1: 
		now=datetime.now()
		# temporary file name is current date and time in DDMMYYHHMMSS.png
		time=now.strftime("%d%m%Y%H%M%S")
		time=time+'.png'
		print(time)
		captured_data=time

		# voice confirmation of capture
		engine.stop()
		engine=pyttsx3.init()
		engine.say('Image captured')
		engine.runAndWait()

		# uploading captured image to azure blob storage
		try:
			# connect to blob
			blob_service_client = BlobServiceClient.from_connection_string(connect_str)

			# container name
			read_data = 'sample-data'
			
			# Save image to temporary file in RPi
			cv2.imwrite(captured_data,image)
			print('Image written')

			# getting blob
			blob_client = blob_service_client.get_blob_client(container=read_data, blob=captured_data)
			container_client = blob_service_client.get_container_client(read_data)

			# upload file
			with open(captured_data, "rb") as data:
				blob_client.upload_blob(data)
			
			# delete temporary file
			os.remove(captured_data)
		except Exception as ex:
			print(ex)
cv2.destroyAllWindows()
