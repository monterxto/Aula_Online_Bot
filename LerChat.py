from threading import Thread, Event
import time
from queue import Queue
class LerMensagens(Thread):
    def __init__(self,evento, infos,driver):
        Thread.__init__(self)
        self.sair = 0
        self.infos_uteis = infos
        self.evento = evento
        self.driver = driver

    def run(self):
      tam = 0
      while True:
        time.sleep(0.4)
        msgs = self.driver.find_elements_by_xpath('//div[@id="chat-history-container"]/ul/li')
        if tam < len(msgs):
          tam = len(msgs)
          p = msgs[len(msgs)-1].find_elements_by_tag_name('p')
          if(p[1].text.upper().startswith('!XTO ')):
            menu = p[1].text.split(" ")
            del(menu[0])
            menu_string = " ".join(menu)
            if menu_string.upper().startswith("PLAY"):
              opcao = menu_string.split(" ")
              self.infos_uteis.put(opcao)
              self.evento.set()
            elif menu_string.upper().startswith("SKIP"):
              opcao = menu_string.split(" ")
              self.infos_uteis.put(opcao)
              self.evento.set()
            elif menu_string.upper().startswith("EXIT"):
              opcao = menu_string.split(" ")
              self.infos_uteis.put(opcao)
              self.evento.set()
            elif menu_string.upper().startswith("LISTA"):
              opcao = menu_string.split(" ")
              self.infos_uteis.put(opcao)
              self.evento.set()
            elif menu_string.upper().startswith("HELP"):
              opcao = menu_string.split(" ")
              self.infos_uteis.put(opcao)
              self.evento.set()

