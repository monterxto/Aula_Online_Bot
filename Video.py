from threading import Thread, Event
import os
import time
import youtube_dl
from datetime import datetime, timedelta
class VideoOperacoes(Thread):
  def __init__(self, event):
      Thread.__init__(self)
      self.primeiro = 0
      self.evento = event
      self.url = []

      self.InicioVideo = 0
      self.DuracaoVideo = 0

      self.VerificarVideo = 0
  def run(self):
      while True:
        if len(self.url) > 0:
          self.InicioVideo = datetime.now()
          try:
            os.system('youtube-dl -o - "'+self.url[0]+'" | vlc -')
          except:
            pass

  def SkipVideo(self):
    os.system('taskkill /f /im vlc.exe')

  def ValidarUrl(self,url):
    extrair = youtube_dl.extractor.gen_extractors()
    for e in extrair:
      if e.suitable(url) and e.IE_NAME != 'generic':
        return False
    return True

  def InfoVideo(self):
    info = youtube_dl.YoutubeDL().extract_info(self.url[0], download=False)
    self.DuracaoVideo = info['duration']
    self.VerificarVideo.setValores(self.InicioVideo,self.DuracaoVideo)
    del(self.url[0])

  def VideoAcabou(self):
    if(self.primeiro == 0):
      self.primeiro = 1
      return 2
    else:
      tempoAgora = datetime.now()
      if tempoAgora - self.InicioVideo >= timedelta(seconds=self.DuracaoVideo):
        return 1
      else:
        return 0

  def FilaVideos(self,url):
    self.url.append(url)

  def setObjeto(self, obj):
    self.VerificarVideo = obj

  def getLista(self):
    if len(self.url) > 0:
      TituloVideo = []
      for video in self.url:
        ProximosVideos = youtube_dl.YoutubeDL().extract_info(video, download=False)
        TituloVideo.append(ProximosVideos['title'])
      return TituloVideo
    else:
      return ["Não Existe Próximos Vídeos"]

  def ListaViva(self):
    if len(self.url) > 0:
      return True
    else:
      return False

