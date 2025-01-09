import pyautogui
import time

#Auf meinem zweiten Bildschirm (links) gehen die Positionen von (-1700,190) bis (-875, 1350)  (oben links bis unten rechts)

#Der Punkt hat den Radius 2, ansonsten unverändert.
#der DINA4-Zettel ist auf dem Bildschirm mit der Auflösung ? im Vollbild bei 33,33%

#Point(x=-1308, y=873) auf diesen Punkt habe ich geklickt. (Viertel Hoch)
#Point(x=-1308, y=822) auf diesem Punkt war der Kringel.
#Rel(0,51) Wenn der Kringel an Stelle x stehen soll, muss ich relativ dazu klicken.

#in meiner Standarteinstellung ist die Bewegung von Rel(1,1) für Gimp (3,3)
#bedeutet, dass jeder Pixel in Python 3 Pixeln in Gimp entsprechen.


def drawLines():
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


drawLines()

#pyautogui.moveTo(-1600,365)
#pyautogui.click()

#Hoch (bis auf 3)
#pyautogui.moveTo(-1400,365) liegt auf der zweiten Linie von oben
#y+7 liegt die Note auf der nächsten Linie
#pyautogui.moveTo(-1300,369) liegt zwischen 2 und 3

#Tief (ab unter 3)
#pyautogui.moveTo(-1100,358) liegt zwischen der 3 und 4
#pyautogui.moveTo(-1010,361) liegt auf der 4
#y+7 ist auf/zwischen der nächsten Linie
