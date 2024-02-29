import pandas as pd
import webbrowser as web
import pyautogui as pg
import time 

celular_d = "921297778"
nombre_d = "Jorge"
nombre_e = "Gabriel"


mensaje = "Hola "+ nombre_d + " mi nombre es "+ nombre_e

chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

web.get(chrome_path).open("https://web.whatsapp.com/send?phone=" + celular_d + "&text=" + mensaje)

time.sleep(15)
pg.click(-46,864)