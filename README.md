# CAM BRAILLE
## INTRODUCTION
The major sensory organ of a person is their eyes. One glimpse around us is enough to make us realize how vision provides most of the information in our environment. 

Timetables in train stations, signs indicating the right way or potential danger, a billboard advertising a new product in the market, these are all the visual types of information we all come across in our daily life. 

Most of this information is inaccessible for the blind and the visually impaired, inhibiting their independence, since access to information signifies autonomy.

## VISION AT YOUR FINGERTIPS
The human eye is like a camera that receives and focuses light into retina which is then transmitted to the brain.

Without retina, eye cannot see thus render vision impossible , hence the visual impairmnent which results difficulties in doing daily simple tasks .

This is where we step in to make sure that the ones who are suffering from visual impairment are at ease  through our Cam Braille.

## CAM BRAILLE  
Cam braille is a device that simply needs to be shown the text that an individual wants to hear
As it's a wearable device , it will be worn at the finger-tip where a small camera will be located for capturing images
Can be worn as wristband which includes the micro-controller
The general working of this device is that  the finger-tip camera will capture the image of the text at which it is pointed  and it will process the text through tts for audio conversion and read it out to our user
it later on uploads the image on cloud storage from where it can be fetched to a website

## FEATURES
Audio dictation of captured text in real-time
Connectivity to any wired headset as well as any Bluetooth speaker/headphones
Cloud storage and website display of captured information for future reference

## Working: Audio dictation of captured text in real-time
Image capturing of desired text
Text recognition from captured image
Text to speech conversion

Cam Braille utilizes a PiCamera to capture an image of the desired text. Subsequently using PyTesseract as OCR, the project reads text from the captured image. An audio dictation is generated in a connected audio device using text to speech conversion via Pyttsx3 TTS.

## Working: Cloud storage and website display of captured information for future reference
Upload of captured image to cloud storage
Fetching uploaded images to web application

The image captured by PiCamera is uploaded to Azure Blob Storage as a blob in a designated Container. All uploaded images are directly fetched to a web application from the blob storage using Azure Functions with a HTTP Trigger for easy future reference.

## SCOPE
Cam Braille can be incorporated into a ring with the camera reading whatever the finger points at.

This is in accordance with Braille reading where the blind use their fingers to read, aimed at adjusting to their standard practices and level of comfort.

The camera can be remodelled to identify other objects and pictures as well, that can help a blind person navigate in daily life

## LINK

[https://www.youtube.com/watch?v=71VuaBb_Go8](https://www.youtube.com/watch?v=71VuaBb_Go8)