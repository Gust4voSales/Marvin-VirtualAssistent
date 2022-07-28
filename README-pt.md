<h1 align="center">
Marvin
</h1>

<p align="center">Assistente virtual que consegue abrir sites e fazer pesquisas neles, abrir programas, tocar música, adicionar lembretes e adicionar novos comandos de voz
  sem precisar mexer com código </p>
👉Link no Youtube demonstrando o bot: https://youtu.be/jjMbnQShabM

## 📜 Sobre
Esse projeto utiliza uma biblioteca de reconhecimento de voz para automatizar as ações que estão no arquivo ```commands.json```, dessa forma, é possível adicionar mais comandos
de voz no arquivo e o assistente irá conseguir executar essas ações sem precisar alterar o código, já que a maioria das ações são dinâmicas (você consegue abrir qualquer site 
que quiser, adicionar um comando para abrir qualquer programa que tiver, etc)

Módulos:
 - **OpenModule**: abra sites e faça pesquisas neles, abra programas, recarregue o arquivo ```commands.json``` para atualizar as moficações feitas;
 - **MusicModule**: toque música (irá pegar o primeiro resultado da pesquisa do Youtube), no **player invisível**, dessa forma, o player não vai tirar o foco da sua gameplay quando você pedir uma música por exemplo, pausar, remover música.
 - **AlarmModule**: adicione lembretes.


## 💻 Techs
[//]: # (Add the features of your project here:)
- **SpeechRecognition** — Biblioteca de reconhecimento de fala, com suporte para diversos engines e APIs, online e offline.
- **pyttsx3** — Uma biblioteca de conversão de texto em fala com Python. Ao contrário das bibliotecas alternativas, funciona offline e é compatível com Python 2 e 3.
- **PyDub** — Manipule áudio com uma interface simples e fácil de alto nível.
- **Pytube** — Pytube é uma biblioteca leve, Pythonic, livre de dependência (e utilitário de linha de comando) para baixar vídeos do YouTube.
- **python-vlc** — Bindings para manipular o player de víceo VLC.
- **keyboard** — Tenha controle total do seu teclado com essa biblioteca.

## 🛠 Iniciando
1. Clone esse repositório rodando no terminal ```git clone https://github.com/Gust4voSales/Marvin-VirtualAssistent/ ``` 

### &nbsp; &nbsp;Utilizando Poetry como gerenciador de dependências (recomendado)

2. Instale Poetry (https://python-poetry.org/docs/#installation)
3. Dentro da pasta do projeto, rode ```poetry install```
4. Download e instale o VLC versão 64bit (https://www.videolan.org/vlc/) para o player do MusicModule 
5. Para rodar o assistente sem mostrar uma janela do terminal, abre o terminal na pasta do projeto e rode ```poetry run pythonw main.py```. 
  Então, você pode fechar essa janela do terminal (o programa está rodando em background) 
5. Para rodar normalmente: ```poetry run python main.py```

### &nbsp; &nbsp;Utilizando o pip (default) como gerenciador de dependências (não recomendado)* 

2. Instale as dependências: 
  &nbsp; &nbsp;<div>- ```pip3 install SpeechRecognition``` </div>
  &nbsp; &nbsp;<div>- ```pip3 install PyAudio``` </div>
  &nbsp; &nbsp;<div>- ```pip3 install pyttsx3``` </div>
  &nbsp; &nbsp;<div>- ```pip3 install pydub``` </div>
  &nbsp; &nbsp;<div>- ```pip3 install Pytube``` </div>
  &nbsp; &nbsp;<div>- ```pip3 install keyboard``` </div>
  &nbsp; &nbsp;<div>- Download e instale o VLC versão 64bit (https://www.videolan.org/vlc/) para o player do MusicModule </div>
  &nbsp; &nbsp;<div>- ```pip3 install python-vlc``` </div> <br>  
3. Para rodar o assistente sem mostrar uma janela do terminal, abre o terminal na pasta do projeto e rode ```pythonw main.py```. 
  Então, você pode fechar essa janela do terminal (o programa está rodando em background) 
3. Para rodar normalmente: ```python main.py```

\* Algumas dependências como o pyaudio não estão sendo mantidos e podem não funcionar quando instalados pelo pip ou irão necessitar de mais debugging + pesquisa pra conseguir fazer funcionar :(

