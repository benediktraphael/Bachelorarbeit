import pyautogui
import time

#Auf meinem zweiten Bildschirm (links) gehen die Positionen des Papiers von (-1700,190) bis (-875, 1350)  (oben links bis unten rechts)

#Der Punkt hat den Radius 2, ansonsten unverändert.
#der DINA4-Zettel ist auf dem Bildschirm mit der Auflösung ? im Vollbild bei 33,33%


#clefs = []
#keys = []
#lineBrush = (-150, 200)
#lineStart = (-1645,350)
#lineLength = 715
#systemHeight = 35

def drawLines(lineBrush, lineStart, lineLength, systemHeight):
    
    pyautogui.moveTo(lineBrush)
    pyautogui.click()
    pyautogui.moveTo(lineStart)

    j = 0
    while(j < 10):

        i = 0
        while(i < 5):
            pyautogui.mouseDown()
            pyautogui.moveRel(lineLength,0)
            pyautogui.mouseUp()
            pyautogui.moveRel(-1*lineLength, systemHeight/5)
            i = i+1

        pyautogui.moveRel(0, 1.5*systemHeight)
        j = j+1


def drawClefs(clef, clefs, lineStart, systemHeight):
    match clef:
        case 71:
            offset = 0
            pyautogui.moveTo(clefs[1])

        case 50:
            offset = 0
            pyautogui.moveTo(clefs[0])
    pyautogui.click()
    pyautogui.moveTo(lineStart[0]+4, lineStart[1]+int(2/5*systemHeight)+offset)
    
    j = 0
    while(j < 10):
        pyautogui.click()
        pyautogui.moveRel(0, 2.25*systemHeight)
        j += 1
    return


def drawKey(key, keys, lineStart, systemHeight):
    accidentals_order = [0,3,1,4,2]
    used_clef = [1,3,5,8,10]
    #b: auf Linie um zwischen Linie.
    sharps = [-14, -4, -18, -7, 4]
    flats = [-2, -20,-9,1,-13]
    #select brush
    if(key < 0):
        pyautogui.moveTo(keys[0])
        used_acc = flats
    else:
        pyautogui.moveTo(keys[1])
        used_acc = sharps
    pyautogui.click()

    for j in range(0, 10):
        pyautogui.moveTo(lineStart[0] + 10, lineStart[1]+2/5*systemHeight+2.5*systemHeight*j)
        for i in range(0, key, (-1 if key < 0 else 1)):
            pyautogui.moveRel(0, used_acc[i])
            pyautogui.click()
            pyautogui.moveRel(1/5*systemHeight, -used_acc[i])
    return


def prepareSheet(clef, key, lineBrush, lineLength, systemHeight, lineStart, clefs, keys):
    drawLines(lineBrush, lineStart, lineLength, systemHeight)
    drawClefs(clef, clefs, lineStart, systemHeight)
    drawKey(key, keys, lineStart, systemHeight)
    return


