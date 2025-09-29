#é um processo de automação robótica de processos (RPA)
# que utiliza a biblioteca PyAutoGUI para controlar o mouse e o teclado, 
# permitindo a automação de tarefas repetitivas no computador.
#Ele só roda na máquina local, não em servidores remotos.
#Tem que ter o Python e a biblioteca PyAutoGUI instalados.
#Para instalar a biblioteca PyAutoGUI: pip install pyautogui
import pyautogui
import time #importa a biblioteca time para selecionar o tempo de espera
pyautogui.PAUSE = 1 #Adiciona um delay de 1 segundo entre as ações do PyAutoGUI

#Pega a posição da tela dando coordenadas x e y
print(pyautogui.position())
#Pega o tamanho da tela
print(pyautogui.size())

#Funções do mouse
time.sleep(1) #Espera 1 segundos para você posicionar o mouse
pyautogui.click(x=100, y=100)
#Para especificar qual botão do mouse usar (left, middle, right)
#pyautogui.click(x=100, y=100, button='right')
#pyautogui.doubleClick(x=100, y=100) ou
#pyautogui.click(x=100, y=100, clicks=2, interval=0.25)
#interval=0.25 #tempo entre os cliques
pyautogui.moveTo(x=200, y=200, duration=1) #move o mouse para a posição escolhida em 1 segundo(duration)
#Nesse caso especialmente em um site que tenha um menu que apareça ao passar o mouse
pyautogui.click






