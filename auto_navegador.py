#Automatiza os navegadores Webdriver
#Instalação: py -m pip install selenium

import selenium

from selenium import webdriver
import time

#Abrir o navegador
navegador = webdriver.Chrome()
#Esse é o tempo que o ficará aberto
time.sleep(5)

#Colocar o navegador em tela cheia
navegador.maximize_window()

#Acessar um site
navegador.get('https://ge.globo.com/')

#Seleciona um elemento no site
botao_menu = navegador.find_element("class name", "menu-button")

#Clica no elemento selecionado
botao_menu.click()

#Esperar antes de fechar o navegador
time.sleep(5)