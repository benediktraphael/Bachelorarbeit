import pyautogui
import time

#Auf meinem zweiten Bildschirm (links) gehen die Positionen des Papiers von (-1700,190) bis (-875, 1350)  (oben links bis unten rechts)

#Der Punkt hat den Radius 2, ansonsten unverändert.
#der DINA4-Zettel ist auf dem Bildschirm mit der Auflösung ? im Vollbild bei 33,33%

def drawLines():
    #select line-brush (-150, 200)
    pyautogui.moveTo(-150, 200)
    pyautogui.click()
    pyautogui.moveTo(-1645,350)

    j = 0
    while(j < 10):

        i = 0
        while(i < 5):
            pyautogui.mouseDown()
            pyautogui.moveRel(715,0)
            pyautogui.mouseUp()
            pyautogui.moveRel(-715, 7)
            i = i+1

        pyautogui.moveRel(0, 50)
        j = j+1


#drawLines()
