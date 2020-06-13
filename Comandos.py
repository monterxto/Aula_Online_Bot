from threading import Thread, Event
from selenium.webdriver.common.keys import Keys
import time
from queue import Queue

class PlayVideo(Thread):
  def __init__(self, obj):
    Thread.__init__(self)
    self.obj = obj
    self.url = 0
    self.evento = 0

  def run(self):
    while True:
      self.Evento.wait()
      self.Evento.clear()
      if not self.obj.ValidarUrl("https://www."+self.url):
        if self.obj.VideoAcabou() == 2:
          self.obj.FilaVideos("https://www."+self.url)
          self.obj.InfoVideo()
        elif self.obj.VideoAcabou() == 1:
          self.obj.SkipVideo()
          self.obj.FilaVideos("https://www."+self.url)
          self.obj.InfoVideo()
        elif self.obj.VideoAcabou() == 0:
          self.obj.FilaVideos("https://www."+self.url)
      else:
        print("não valido")

  def setUrl(self,url):
    self.url = url

  def setEvento(self,evento):
    self.Evento = evento


class SkipVideo(Thread):
  def __init__(self, obj):
    Thread.__init__(self)
    self.obj = obj
    self.Evento = 0

  def run(self):
    while True:
      self.Evento.wait()
      self.Evento.clear()
      self.obj.SkipVideo()
      if len(self.obj.url) > 0:
        self.obj.InfoVideo()

  def setEvento(self,evento):
    self.Evento = evento

class Lista(Thread):
  def __init__(self, obj, driver, nomeElem):
    Thread.__init__(self)
    self.obj = obj
    self.driver = driver
    self.nomeElem = nomeElem
    self.Evento = 0

  def run(self):
    while True:
      self.Evento.wait()
      self.Evento.clear()
      self.driver.implicitly_wait(50)
      self.nomeElem.send_keys("Lista dos Próximos vídeos:")
      self.nomeElem.send_keys(Keys.ENTER)
      i = 1
      for msg in self.obj.getLista():
        self.driver.implicitly_wait(50)
        self.nomeElem.send_keys("{}) {}".format(i,msg))
        self.nomeElem.send_keys(Keys.ENTER)
        i += 1

  def setEvento(self,evento):
    self.Evento = evento

class HelpBot(Thread):
  def __init__(self, driver,nomeElem):
    Thread.__init__(self)
    self.driver = driver
    self.nomeElem = nomeElem
    self.Evento = 0

  def run(self):
    while True:
      self.Evento.wait()
      self.Evento.clear()

      self.driver.implicitly_wait(50)
      self.nomeElem.send_keys("Eu sou um bot de Video e Música")
      self.nomeElem.send_keys(Keys.ENTER)
      self.driver.implicitly_wait(50)
      self.nomeElem.send_keys("Adicionar um vídeo na fila: !xto play <url do video>")
      self.nomeElem.send_keys(Keys.ENTER)
      self.driver.implicitly_wait(50)
      self.nomeElem.send_keys("Passar o Vídeo: !xto skip")
      self.nomeElem.send_keys(Keys.ENTER)
      self.driver.implicitly_wait(50)
      self.nomeElem.send_keys("Listar os Vídeos da fila: !xto lista")
      self.nomeElem.send_keys(Keys.ENTER)
      self.driver.implicitly_wait(50)
      self.nomeElem.send_keys("Ajuda: !xto help")
      self.nomeElem.send_keys(Keys.ENTER)
      self.driver.implicitly_wait(50)
      self.nomeElem.send_keys("Fechar: !xto exit")
      self.nomeElem.send_keys(Keys.ENTER)

  def setEvento(self,evento):
    self.Evento = evento