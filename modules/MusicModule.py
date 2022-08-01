import threading
from pytube import YouTube
import vlc
from time import sleep
import Marvin
import re, urllib.parse, urllib.request


# VLC LIB function that will play locally in another thread
class MusicPlayerTask:
  def __init__(self):
    self.Instance = vlc.Instance()

    self._playing = False
    self.pause = False

  def stop_player(self):
    self._playing = False

  def toggle_pause_song(self):
    self.pause = not self.pause
    
  def reset(self):
    self._playing = False
    self.pause = False

  def play(self, music_url):
    Media = self.Instance.media_new(music_url)
    Media.get_mrl()

    player = self.Instance.media_player_new()
    player.set_media(Media)
    player.play()
    self._playing = True
  
    while self._playing:
      sleep(0.1)
      while player.is_playing():
        if not self._playing:
          player.stop()
          break
        if self.pause:
          player.pause() # this leaves the loop, since player.is_playng == False
          break # just to make sure (lol)
        
        sleep(0.1)
      if not self._playing:
        player.stop()
        break
      if not self.pause:
        player.play()
    
    self.reset()

music_player = MusicPlayerTask()

def parse_command(command_action, argument=''):
  global music_thread, pause_music_thread
  if command_action=='tocar':
    if (music_player._playing): # already playing something (even if it's paused)
      if (argument=='a música' or argument==''):  # unpause current song (somenthing like 'toque a música')
        music_player.toggle_pause_song()
      else:
        # stop current song and replace it
        stop_music() 
        play_music(argument)
    else: 
      if (argument=='a música'): # play a new song 
        play_music('system of a down')
      else: # play a new song (specific)
        play_music(argument)

  if music_player._playing:
    if command_action=='pausar':
      pause_music()
    elif command_action=='fechar':
      stop_music()

def get_music_youtube_link(music_name):
  Marvin.speak('Procurando por ' + music_name)
  
  query_string = urllib.parse.urlencode({"search_query": music_name})
  formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
  search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
  # clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
  clip = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])
  return clip

def play_music(music_name):
  global playing_song
  clip = get_music_youtube_link(music_name)
  print(clip)

  # get audio 
  yt = YouTube(clip)
  music_url = yt.streams.filter(only_audio=True).first().url
  # out_file = yt.streams.filter(only_audio=True).first().download() # to download the music

  # start play music thread
  music_thread = threading.Thread(target=music_player.play, args=(music_url, ), daemon=True)
  music_thread.start()

    # webbrowser.get('windows-default').open_new(clip) # open youtube music
def pause_music():
  music_player.toggle_pause_song()

def stop_music():
  music_player.stop_player()

