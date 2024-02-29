import pandas as pd
import webbrowser as web
import pyautogui as pg
import time 

data = pd.read_excel("base02.xlsx" , sheet_name='personas')
data.head(4)
ruta_img = "C:/Users/MARGARITA VITE/Downloads/imagen_proyecto_PY"

for i in range(len(data)):
    print(i)
    celular = str(int(data.loc[i,'TELEFONOS']))
    nombre = data.loc[i,'NOMBRES']

    mensaje = "Hola " + nombre + " feliz día de la amistad"

    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

    web.get(chrome_path).open("https://web.whatsapp.com/send?phone=" + celular + "&text=" + mensaje)

    time.sleep(30) 
    pg.click(-1092,865) 
    time.sleep(3)   
    pg.click(-1026,579) 
    time.sleep(3)   
    pg.click(-1150,68)
    time.sleep(3)
    pg.write(ruta_img) 
    time.sleep(4)
    pg.click(-1046,64) 
    time.sleep(3)
    pg.click(-1335,235)
    time.sleep(3)
    pg.press('enter')
    time.sleep(3)
    pg.press('enter')
    time.sleep(5) 
