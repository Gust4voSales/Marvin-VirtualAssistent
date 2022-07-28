[README em Português](https://github.com/Gust4voSales/Marvin-VirtualAssistent/blob/master/README-pt.md)
<h1 align="center">
Marvin
</h1>

<p align="center">Virtual assistent that can open websites and do researchs on them, open programs, play music, set reminders and add new voice commands without need to code</p>
👉Youtube link demonstrating the bot: https://youtu.be/jjMbnQShabM

## 📜 About
This project uses a voice recognition library to automate actions from the ```commands.json``` file, this way, we can add more voice commands to the file and the assistent will be 
able to do those tasks without changing the code, since most of the tasks are dinamic (you can open up any website you want, 
add a command to open any program you have locally, etc)

Modules:
 - **OpenModule**: open websites and do research inside them, open programs, reload the ```commands.json``` to update the modifications added;
 - **MusicModule**: play music (it's going to get the music from the Youtube's first result) in an **invisible player**, this way it won't remove focus from your gameplay when you request a song for example, pause song, remove song.
 - **AlarmModule**: set reminders


## 💻 Techs
[//]: # (Add the features of your project here:)
- **SpeechRecognition** — Library for performing speech recognition, with support for several engines and APIs, online and offline.
- **pyttsx3** — A text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.
- **PyDub** — Manipulate audio with a simple and easy high level interface.
- **Pytube** — Pytube is a lightweight, Pythonic, dependency-free, library (and command-line utility) for downloading YouTube Videos.
- **python-vlc** — Bindings to manipulate vlc player.
- **keyboard** — Take full control of your keyboard with this small Python library.

## 🛠 Getting started
1. Clone this repo running on your terminal ```git clone https://github.com/Gust4voSales/Marvin-VirtualAssistent/ ``` 

### &nbsp; &nbsp;Using poetry package manager (recommended)

2. Install Poetry (https://python-poetry.org/docs/#installation)
3. Inside the project folder run ```poetry install```
4. Download and install VLC 64bit version (https://www.videolan.org/vlc/) for the MusicModule player
5. To run the assistent without showing a terminal window, run ```poetry run pythonw main.py```. 
  Then you can close this terminal window (the program is running in the background) 
5. To run normally: ```poetry run python main.py```

### &nbsp; &nbsp;Using pip default package manager (not recommended)* 

2. Install all dependencies: 
  &nbsp; &nbsp;<div>- ```pip3 install SpeechRecognition``` </div>
  &nbsp; &nbsp;<div>- ```pip3 install PyAudio``` </div>
  &nbsp; &nbsp;<div>- ```pip3 install pyttsx3``` </div>
  &nbsp; &nbsp;<div>- ```pip3 install pydub``` </div>
  &nbsp; &nbsp;<div>- ```pip3 install keyboard``` </div>
  &nbsp; &nbsp;<div>- ```pip3 install Pytube``` </div>
  &nbsp; &nbsp;<div>- Download and install VLC 64bit version (https://www.videolan.org/vlc/) for the MusicModule player </div>
  &nbsp; &nbsp;<div>- ```pip3 install python-vlc``` </div> <br>  
3. To run the assistent without showing a terminal window, then open up the terminal on the project folder and run ```pythonw main.py```. 
  Then you can close this terminal window (the program is running in the background) 
3. To run normally: ```python main.py```
\* Some dependencies such as pyaudio are not being manteined properly and may not work when installed through pip or require more debugging + searching in order to make it work :(

