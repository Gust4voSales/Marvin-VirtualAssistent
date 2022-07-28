from time import sleep
import speech_recognition as sr # recognise 
import keyboard  
import Marvin

recognizer = sr.Recognizer()

# sometimes the recognizer confuses Marvin with these names
BOT_NAMES = ['marvin', 'marlin', 'mavin', 'marli', 'martin', "mommy" ]

def record_audio():
  with sr.Microphone() as source: # microphone as source
    audio = recognizer.listen(source, None, 3)  # listen for the audio via source
    voice_data = ''

    try:
      voice_data = recognizer.recognize_google(audio, language="en-US").lower()  # convert audio to text
    except sr.UnknownValueError: # error: recognizer does not understand
      print()
    except sr.RequestError:
      print('Serviço offline') # error: recognizer is not connected

    print(">>", voice_data) # print what user saidprint
    for bot_name_variation in BOT_NAMES:
      if (bot_name_variation in voice_data):
        Marvin.listen()
        break

# while True:
#   record_audio()
while True:
  sleep(0.05) # sleep function prevents loop from being called multiple time and increasing CPU usage
  if keyboard.is_pressed('ctrl+alt+m'):
    Marvin.listen()
  sleep(0.05) # sleep function prevents loop from being called multiple time and increasing CPU usage

