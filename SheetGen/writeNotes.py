import math
import pyautogui
import time
from processMidiNumbers import processMidiNumbers



def helperLines(steps):
    '''
    draws the helperlines for the note

    Params:
        steps(int): number of steps, the note takes
    
    Returns:
        null
    '''

    pos = pyautogui.position()
    pyautogui.moveTo(-180, 200)#helpLine-Brush
    pyautogui.click()

    pyautogui.moveTo(pos)


    if(steps > 0):
        v = -1
    else:
        v = 1

    #move to upper or lower line
    pyautogui.moveRel(0, v*14)

    for i in range(0, abs(int(steps/2))-2):
        pyautogui.moveRel(0, v*7)
        pyautogui.click()

    pyautogui.moveTo(pos.x, pos.y)
    return


def writeSheetMusic(key, clef, midiNotes):

    '''Preparation'''
    midiDict = {}
    processMidiNumbers(key, clef, midiNotes, midiDict)
    

    '''Positions of brushes'''
    brushes = [(-150, 175), (-115, 175), (-115, 140), (-80, 140), (-80, 175), (-45, 175), (-45, 140), (-180, 175)]
    additional_brushes = [(-180, 200), (-150, 200)]


    '''constant x-shift per 1/16 and number of 1/16 per System'''
    note_width = 12
    counter = 200
    
    '''
    Wann liegen Hoch Tief auf der Mittellinie?
        pyautogui.moveTo(x, 373) dann ist Hoch mittig
        pyautogui.moveTo(x, 355) dann ist Tief mittig

    Ergo:
        Hoch-Offset: 23
        Tief-Offset: 5
    '''
    high_offset = 9
    low_offset = -9

    '''bring mouse in the right position'''
    pyautogui.moveTo(-1500, 364+85*3)

    for note in midiNotes:

        steps = midiDict[note[1]][0]
        '''Brushes Index: 2 * log2(Länge (in Sechszehntel)) + (Tief?)'''
        brush = int(2*math.log2(note[0]) + (1 if steps < 0 else 0))#Punktierte Noten fehlen noch


        '''Select correct brush''' 
        cur_pos = pyautogui.position()
        pyautogui.moveTo(brushes[brush])
        pyautogui.click()
        pyautogui.moveTo(cur_pos)
        
        '''Calculate y-shift'''
        if(steps < 0):
            y = -1 * (7 * int(steps/2) - (steps % 2) * 4)+low_offset

        else:
            y = -1 * (7 * int(steps/2) + (steps % 2) * 3)+high_offset
        

        '''Paint the Note and Helperlines'''
        pyautogui.moveRel(0, y)
        pyautogui.click()
        pyautogui.moveRel(0, -y)
        if(abs(int(steps/2)) > 2):
            helperLines(steps)
        

        '''shift on the x-axes'''
        pyautogui.moveRel(note_width*note[0], 0)
        counter -= note[0]
        '''move to next system'''
        if(counter <= 0):
            '''
            Um auf die Mittellinie des x-ten 5-Zeilensystems zu kommen:
                Hoch: y = 372+85x
                Tief: y = 355+85x
            '''
            pyautogui.moveRel(-1*(abs(counter) + 20)*note_width, 85)
            counter = 200
            
    return

time.sleep(3)
midiNotes = [(4, 60, 0), (4, 62, 0), (8, 64, 0), (4, 65, 0), (2, 67, 0), (2, 69, 0), (1, 71, 0), (1, 72, 0)]
writeSheetMusic(0, 71, midiNotes)
pyautogui.moveTo(-1000, 364)
helperLines(-8)
'''
#Ich erwarte eine Liste an Noten mit der Form
#(Position (in 1/16), Ton(ohne Vorzeichen), Vorzeichen(null, b, #), Dauer (in 1/16)) 
#Bsp. (8, C4, null, 4 ):
#bedeutet: C4 wird 8/16 nach Begin (nach 2 viertel) für 4/16 (ein Viertel) gespielt.

#Da ich eine Melodie erwarte, sollte es zu keiner Überlappung kommen.

#pyautogui.moveTo(-1645,364)




    #while clef(startIndex+i < Steps): i++
    #Steps - (startIndex+i)%5

    #these show the Order, in which the accidentals are changed. for Treble
'''

'''
Ermitteln der Positionen (Wo sind die Pinsel?)
Achtel
    Hoch (-115, 140)
    Tief (-80, 140)
Halbe
    Hoch (-45, 140)
    Tief (-180, 175)
Sechszehntel
    Hoch (-150, 175)
    Tief (-115, 175)
Viertel
    Hoch (-80, 175)
    Tief (-45, 175)
Zusatz
    Hilfslinie (-180, 200)
    Pinsel (-150, 200)
    Vorzeichen
    ...
    Pausen
    ...
    
Speicher in Array an Index
2 * log2(Länge (in Sechszehntel)) + (Tief?)  ... 2^x Sechszehntel lang
    Bsp. Achtel Hoch = 2 * 1 + 0
Wenn Pausen dazu kommen (3 * log + 0 (h) 1(tief) 2(pause))
'''

''' 
#pyautogui.moveTo(-1500, 355+85)
#writeSheetMusic(0, 71, midiNotes)
#riteNotes()
#Hoch (bis auf 3)
#pyautogui.moveTo(-1400,365) liegt auf der zweiten Linie von oben
#y+7 liegt die Note auf der nächsten Linie
#pyautogui.moveTo(-1300,369) liegt zwischen 2 und 3

#Tief (ab unter 3)
#pyautogui.moveTo(-1100,358) liegt zwischen der 3 und 4
#pyautogui.moveTo(-1010,361) liegt auf der 4
#y+7 ist auf/zwischen der nächsten Linie




#Auf meinem zweiten Bildschirm (links) gehen die Positionen von (-1700,190) bis (-875, 1350)  (oben links bis unten rechts)

#Der Punkt hat den Radius 2, ansonsten unverändert.
#der DINA4-Zettel ist auf dem Bildschirm mit der Auflösung ? im Vollbild bei 33,33%

#Point(x=-1308, y=873) auf diesen Punkt habe ich geklickt. (Viertel Hoch)
#Point(x=-1308, y=822) auf diesem Punkt war der Kringel.
#Rel(0,51) Wenn der Kringel an Stelle x stehen soll, muss ich relativ dazu klicken.

#in meiner Standarteinstellung ist die Bewegung von Rel(1,1) für Gimp (3,3)
#bedeutet, dass jeder Pixel in Python 3 Pixeln in Gimp entsprechen.
'''