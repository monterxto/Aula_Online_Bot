from threading import Thread, Event
import os
import time
import youtube_dl
from datetime import datetime, timedelta

class VerificarVideoVivo(Thread):
  def __init__(self, video):
      Thread.__init__(self)
      self.primeiro = 0
      self.InicioVideo = 0
      self.DuracaoVideo = 0

      self.video = video

  def run(self):
    while True:
      time.sleep(5)
      if self.video.ListaViva():
        if self.DuracaoVideo != 0:
          tempoAgora = datetime.now()
          if tempoAgora - self.InicioVideo >= timedelta(seconds=self.DuracaoVideo):
            self.video.SkipVideo()
            if len(self.video.url) > 0:
              self.video.InfoVideo()
            
  def setValores(self,inicio,duracao):
    self.InicioVideo = inicio
    self.DuracaoVideo = duracao
