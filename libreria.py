import pyautogui
import time
#screenWidth, screenHeight = pyautogui.size() # Devuelve dos números enteros, el ancho y el alto de la pantalla. (El monitor principal, en configuraciones de varios monitores).
#print(screenWidth)
#print(screenHeight)
while (True):
    currentMouseX, currentMouseY = pyautogui.position() # Devuelve dos números enteros, la x y la y de la posición actual del cursor del mouse.
    print(currentMouseX)
    print(currentMouseY)
    time.sleep(3)