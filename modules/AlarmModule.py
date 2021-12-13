import threading
import time
import Marvin
from pydub.playback import play
from pydub import AudioSegment
from utils import text2int
import re
from datetime import date, datetime, timedelta 


# TEXT_TO_SECONDS = { "um minuto": 60, "" }
unities_to_secs = { "horas": 3600, "hora": 3600, "minuto": 60, "minutos": 60, "segundos": 1, "segundo": 1 }
ALARM_SOUND = AudioSegment.from_wav("modules/alarm.wav")

class CountdownTask:
  def __init__(self, purpose):
    self._running = True
    self.purpose = purpose

  def terminate(self):
    self._running = False

  def run(self, n):
    while self._running and n > 0:
      n -= 1
      time.sleep(1)
    else:
      play(ALARM_SOUND)
      Marvin.speak("Está na hora de lembrar de " + self.purpose)

def parse_command(command_action, argument, when):
  print(command_action, ', ', argument, ', ', when) 
  # cancelar o ultimo alarme, cancelar todos
  # if when = '' -> error 
  if len(when)==0:
    return
  if command_action['type']=='in':
    text = when
    if when[0]=='a':
      text = when[1:].strip()

    seconds = text2seconds(text)
    set_alarm_in(seconds, argument)
    timeToAlarm = (datetime.now() + timedelta(seconds=seconds)).strftime("%H:%M")
    Marvin.speak("Alarme anotado para às " + timeToAlarm)

def text2seconds(text):
  # print(text) 
  if ':' in text: # hour in hh:mm format
    time_obj = time.strptime(text.strip(), '%H:%M')
    print(time_obj.tm_hour, time_obj.tm_min, time_obj.tm_sec)
    return (time_obj.tm_hour*3600) + (time_obj.tm_min*60)
  else: # 3 horas e 40 minutos -> 3 horas e quarenta minutos
    result = 0

    for index, word in enumerate(text.split(' ')):
      if word in unities_to_secs: # word == minutos for example        
        number = 0
        if text.split(' ')[index-1].isnumeric():
          number = int(text.split(' ')[index-1])
        else: 
          number = text2int.run(text.split(' ')[index-1].strip())
          
        result += unities_to_secs[word] * number
    
    # adicionar segundos sem ter dito "segundos" se for setados tipo 2minutos e 10
    if word.isnumeric(): # word is the last word from loop
      result += int(word)
    else:
      result += text2int.run(word) # text2int returns 0 if the word is not a number

    if 'e meia' in text:
      result += 1800 # + 30 minutos
    if 'meia hora' in text:
      result += 1800 # + 30 minutos


  return result


def set_alarm_in(seconds, argument):
  c = CountdownTask(argument)
  # create countdown thread
  t = threading.Thread(target=c.run, args=(seconds, ), daemon=False) 
  t.start()
  print('clock started, secs --> ', seconds)


def extract_argument_with_time(command_text, voice_command, time_indicator):
  # time_indicator_pos = command_text.find(time_indicator)
  regex_time_indicator = rf"\b{time_indicator}\b"
  time_indicator_pos = -1

  time_indicator_search = re.search(regex_time_indicator, command_text)
  if (time_indicator_search != None):
    time_indicator_pos = time_indicator_search.start()

  if time_indicator_pos==-1:
    return ['', '']
  
  when = command_text[time_indicator_pos+len(time_indicator):].strip()

  command_text_without_when = command_text[:time_indicator_pos].strip()
  
  voice_command_without_when = ''
  time_indicator_voice_command_search = re.search(regex_time_indicator, voice_command)
  if time_indicator_voice_command_search != None:
    voice_command_without_when = voice_command[:time_indicator_voice_command_search.start()].strip()
  
  splitted_text_with_argument = command_text_without_when.split(voice_command_without_when.replace('*', '') , 1)

  argument = ''
  if len(splitted_text_with_argument) > 1:
    argument = splitted_text_with_argument[1]
  else:
    argument = splitted_text_with_argument[0]

  return [argument, when]

