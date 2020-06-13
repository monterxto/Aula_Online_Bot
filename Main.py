from IniciarBot import IniciarScript
from LerChat import LerMensagens
from Video import VideoOperacoes
from VerificarVideoVivo import VerificarVideoVivo
from threading import Thread, Event, main_thread
from queue import Queue
from selenium.webdriver.common.keys import Keys
from Comandos import PlayVideo, SkipVideo, Lista, HelpBot 
import sys
import time

#Script para o bot logar e mandar a msg...
driver = IniciarScript()

#Variáveis uteis
driver.implicitly_wait(50)
nomeElem = driver.find_element_by_id("message-input")
infos_uteis = Queue()

#Eventos
evento = Event()
AddVideoEvent = Event()
PassarVideoEvent = Event()
ListarVideosEvent = Event()
HelpEvent = Event()

#Instanciando as Classes
leitor = LerMensagens(evento, infos_uteis,driver)
video = VideoOperacoes(evento)
VerificarVideo = VerificarVideoVivo(video)
video.setObjeto(VerificarVideo)

#Threads Comandos
AddVideo = PlayVideo(video)
PassarVideo = SkipVideo(video)
ListarVideos = Lista(video,driver,nomeElem)
BotHelp = HelpBot(driver,nomeElem)

AddVideo.setEvento(AddVideoEvent)
PassarVideo.setEvento(PassarVideoEvent)
ListarVideos.setEvento(ListarVideosEvent)
BotHelp.setEvento(HelpEvent)

if __name__ == '__main__':
  #Iniciando as Thread
  leitor.daemon = True
  video.daemon = True
  VerificarVideo.daemon = True
  AddVideo.daemon = True
  PassarVideo.daemon = True
  ListarVideos.daemon = True
  BotHelp.daemon = True
  leitor.start()
  video.start()
  VerificarVideo.start()
  AddVideo.start()
  PassarVideo.start()
  ListarVideos.start()
  BotHelp.start()
  while True:
    evento.wait()
    evento.clear()

    menu = infos_uteis.get()
    if menu[0].upper() == "PLAY":
      AddVideo.setUrl(menu[1])
      AddVideoEvent.set()
    elif menu[0].upper() == "SKIP":
      PassarVideoEvent.set()
    elif menu[0].upper() == 'LISTA':
      ListarVideosEvent.set()
    elif menu[0].upper() == 'HELP':
      HelpEvent.set()
    elif menu[0].upper() == 'EXIT':
      nomeElem.send_keys("Tchau!")
      nomeElem.send_keys(Keys.ENTER)
      try:
        video.SkipVideo()
      except:
        pass
      sys.exit()
