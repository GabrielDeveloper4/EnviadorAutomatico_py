import pandas as pd
import webbrowser as web
import pyautogui as pg
import time 

data = pd.read_excel("base01.xlsx" , sheet_name='personas')
data.head(4)

for i in range(len(data)):
    print(i)
    celular = str(int(data.loc[i,'TELEFONOS']))
    nombre = data.loc[i,'NOMBRES']

    mensaje = "Hola " + nombre

    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

    web.get(chrome_path).open("https://web.whatsapp.com/send?phone=" + celular + "&text=" + mensaje)

    time.sleep(15)
    pg.click(-51,860)
    time.sleep(5)

