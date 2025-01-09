import pyautogui
import time
#Ich erwarte eine Liste an Noten mit der Form
#(Position (in 1/16), Ton(ohne Vorzeichen), Vorzeichen(null, b, #), Dauer (in 1/16)) 
#Bsp. (8, C4, null, 4 ):
#bedeutet: C4 wird 8/16 nach Begin (nach 2 viertel) für 4/16 (ein Viertel) gespielt.

#Da ich eine Melodie erwarte, sollte es zu keiner Überlappung kommen.

#pyautogui.moveTo(-1645,364)


def processingMidiNumbers(key, clef, midiNotes):
    print("processing")
    #ViolinSchlüssel H4 Midi 71
    #BassSchlüssel D3 Midi 50

    #midiNotes(i)-50: differenz sagt mir (theoretisch) den Abstand


def writeNotes():
    print("writing notes....")

    '''
    Um auf die Mittellinie des x-ten 5-Zeilensystems zu kommen:
        Hoch: y = 372+85x
        Tief: y = 354+85x
    '''

    '''
    Welches Höhenoffset muss jeweils eingestellt werden?
        Hoch:
            auf Linie x über Mittellinie: -7*x
            zwischen Linie x und x+1 über Mittellinie: -7*x - 3
        Tief:
            auf Linie x unter Mittellinie: +7*x
            zwischen Linie x und x+1 unter Mittellinie: +7*x + 4
    '''

    #y = 372 + 85 bringt mich auf die Mittellinie eines 5-Zeilensystems.
    pyautogui.moveTo(-1645,354+85)
    pyautogui.click()

writeNotes()
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
    
Speicher in Array an Index
2 * log2(Länge (in Sechszehntel)) + (Tief?)  ... 2^x Sechszehntel lang
    Bsp. Achtel Hoch = 2 * 1 + 0
Wenn Pausen dazu kommen (3 * log + 0 (h) 1(tief) 2(pause))
'''


