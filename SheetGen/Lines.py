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


def drawClefs(clef):
    match clef:
        case 71:
            offset = 4
            pyautogui.moveTo(-150, 250)

        case 50:
            offset = 0
            pyautogui.moveTo(-180, 250)
    #select Notenschlüssel
    pyautogui.click()
    pyautogui.moveTo(-1630, 364+offset)
    
    j = 0
    while(j < 10):
        pyautogui.click()
        pyautogui.moveRel(0, 85)
        j += 1
    return


def drawKey(key):
    accidentals_order = [0,3,1,4,2]
    used_clef = [1,3,5,8,10]
    #b: auf Linie um zwischen Linie.
    sharps = [-14, -4, -18, -7, 4]
    flats = [-2, -20,-9,1,-13]
    #select brush
    if(key < 0):
        pyautogui.moveTo(-80, 200)
        used_acc = flats
    else:
        pyautogui.moveTo(-45, 200)
        used_acc = sharps
    pyautogui.click()

    for j in range(0, 10):
        pyautogui.moveTo(-1610, 364+85*j)
        for i in range(0, key, (-1 if key < 0 else 1)):
            pyautogui.moveRel(0, used_acc[i])
            pyautogui.click()
            pyautogui.moveRel(7, -used_acc[i])
    return


def prepareSheet(clef, key):
    drawLines()
    drawClefs(clef)
    drawKey(key)
    return

prepareSheet(71,3)