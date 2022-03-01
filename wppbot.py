# 1. Importar bibliotecas necessárias
import pywhatkit
import keyboard
import time  # pausa temporal
from datetime import datetime
# 2. Definir para quais contatos iremos enviar as msgs
contatos = [''] #colocar o número do contato no formato [CódigodoPaís+DDD+Númerodetelefone]
# 3. Definir intervalo de envio para cada contato
while len(contatos) >= 1:
    # enviar mensagens
    pywhatkit.sendwhatmsg(contatos[0],'Bom dia! Como você está hoje? 🌹',datetime.now().hour,
    datetime.now().minute + 1)
    del contatos[0]
    time.sleep(60)
    keyboard.press_and_release('ctrl + w')
