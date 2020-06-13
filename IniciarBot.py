from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from random import shuffle, randint
import time

def IniciarScript():
  chrome_options = Options()
  chrome_options.add_argument("--use-fake-ui-for-media-stream")
  driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=chrome_options)
  driver.get("https://us.bbcollab.com/guest/d3c0bb8b107d4c9092488ff4f6383be7")
  control = 1
  while True:
    try:
      nomeElem = driver.find_element_by_id("guest-name")
      nomeElem.send_keys("Bot Xto")
      nomeElem.send_keys(Keys.ENTER)
      break
    except:
      print('[ERROR] Campo nome não encontrado. Outra tentativa acontecerá em %d' % (control))
      driver.implicitly_wait(control)
    else:
      print('[OK] - Nome digitado com sucesso.')
      control = 0

  #Selecionar o microfone que eu quero
  driver.implicitly_wait(50)
  mic = Select(driver.find_element_by_id('techcheck-audio-mic-select'))
  driver.implicitly_wait(50)
  mic.select_by_visible_text('VoiceMeeter Output (VB-Audio VoiceMeeter VAIO)')

  #Clicar no botão para ignorar
  driver.implicitly_wait(50)
  botao = driver.find_element_by_xpath("//div[@class='techcheck-audio-skip ng-scope']/button")
  driver.implicitly_wait(50)
  botao.click()

  #Selecionar a câmera que eu quero
  driver.implicitly_wait(50)
  cam = Select(driver.find_element_by_id('techcheck-video-cam-select'))
  driver.implicitly_wait(50)
  cam.select_by_visible_text('OBS-Camera')

  #Clicar no botão para prosseguir
  botao = driver.find_element_by_xpath("//div[@class='equal-buttons buttons-2-md ng-scope']/button")
  driver.implicitly_wait(50)
  botao.click()

  #Clicar para fechar o tutorial
  driver.implicitly_wait(50)
  nomeElem = driver.find_element_by_xpath('//*[@id="announcement-modal-page-wrap"]/button')
  nomeElem.click()

  # clicar na aba
  driver.implicitly_wait(50)
  nomeElem = driver.find_element_by_xpath('//*[@id="side-panel-open"]')
  nomeElem.click()


  # clicar em todos
  driver.implicitly_wait(50)
  nomeElem = driver.find_element_by_xpath('//*[@id="chat-channel-scroll-content"]/ul/li/ul/li')
  nomeElem.click()
  
  #Clicar para habilitar o mic
  driver.implicitly_wait(50)
  nomeElem = driver.find_element_by_xpath('//div[@class="controls-container ng-scope"]/span[2]/button')
  driver.implicitly_wait(50)
  nomeElem.click()

  #Clicar para habilitar a cam
  driver.implicitly_wait(50)
  nomeElem = driver.find_element_by_xpath('//div[@class="controls-container ng-scope"]/button[1]')
  driver.implicitly_wait(50)
  nomeElem.click()

  #Confimar para habilitar a cam
  driver.implicitly_wait(50)
  nomeElem = driver.find_element_by_xpath('//div[@class="equal-buttons buttons-2-md ng-scope"]/button[2]')
  time.sleep(3)
  nomeElem.click()

  #Abrir o Arquivo com as frases
  frases = open('./mensagens.txt', 'r')

  # clicar no campo escrever a mensagem, e enviar as mensaens do arquivo aleatoriamente
  time.sleep(3)
  nomeElem = driver.find_element_by_id("message-input")
  lista_frase = []
  for linha in frases:
    lista_frase.append(linha)
  shuffle(lista_frase)
  for i in lista_frase:
    driver.implicitly_wait(50)
    nomeElem.send_keys(lista_frase[i])
    nomeElem.send_keys(Keys.ENTER)

  #Clicar na aba dos integrantes da sala
  driver.implicitly_wait(50)
  abaIntegrantes = driver.find_element_by_id("panel-control-participants")
  abaIntegrantes.click()

  #Escolher um participante da sala e abrir o chat
  driver.implicitly_wait(50)
  usuarios = driver.find_elements_by_xpath('//ul[@class="participant-roster"]/li')
  while True:
    time.sleep(1)
    shuffle(lista_frase)
    nome = usuarios[0].find_element_by_xpath('//span[@class="participant-name ng-binding"]').text
    if not nome.startswith("Bot Xto"):
      driver.implicitly_wait(50)
      botao1 = usuarios[0].find_element_by_xpath('//div[@class="participant-icons__wrap participant-controls-static"]/button')
      driver.implicitly_wait(50)
      botao1.click()
      driver.implicitly_wait(50)
      botao2 = usuarios[0].find_element_by_xpath('//button[@class="button menu-list__control focus-item"]')
      driver.implicitly_wait(50)
      botao2.click()
      break
    else:
      continue

  #Abrir arquivo de mensagensPV e Mandar as mensagensPV
  frasesPV = open('./mensagensPV.txt', 'r')
  time.sleep(3)
  msgsPV = driver.find_element_by_id("message-input")
  lista_frase = []
  for linha in frasesPV:
    lista_frase.append(linha)
  shuffle(lista_frase)
  for i in lista_frase:
    driver.implicitly_wait(50)
    msgsPV.send_keys(i)
    msgsPV.send_keys(Keys.ENTER)

  #Clicar no botão voltar e depois em todos
  driver.implicitly_wait(50)
  voltar = driver.find_element_by_xpath('//button[@class="previous-panel icon-button has-tooltip ng-scope"]')
  voltar.click()
  
  driver.implicitly_wait(50)
  todos = driver.find_element_by_xpath('//*[@id="chat-channel-scroll-content"]/ul/li/ul/li')
  todos.click()

  #Mensagem dizendo que iniciou
  iniciou = driver.find_element_by_id("message-input")
  driver.implicitly_wait(50)
  iniciou.send_keys('Bot Xto Iniciou')
  iniciou.send_keys(Keys.ENTER)

  frases.close()
  frasesPV.close()
  #driver.find_element_by_xpath('//button[@class="button menu-list__control focus-item"]')

  return driver