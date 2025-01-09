import math
import pyautogui
import time
import clefCalculation

#Ich erwarte eine Liste an Noten mit der Form
#(Position (in 1/16), Ton(ohne Vorzeichen), Vorzeichen(null, b, #), Dauer (in 1/16)) 
#Bsp. (8, C4, null, 4 ):
#bedeutet: C4 wird 8/16 nach Begin (nach 2 viertel) für 4/16 (ein Viertel) gespielt.

#Da ich eine Melodie erwarte, sollte es zu keiner Überlappung kommen.

#pyautogui.moveTo(-1645,364)




    #while clef(startIndex+i < Steps): i++
    #Steps - (startIndex+i)%5

    #these show the Order, in which the accidentals are changed. for Treble



def processingMidiNumbers(key, clef, midiNotes):
    '''
        determines relative position of MidiNumber on sheet.
        I know afterwards, how every appearing midiNumber is represented on the sheet

        Args:
            key(int): number of accidentals (+ sharp, - flat); example: G major = +1
            clef(int): MidiNumber of the note, which is on the center-line in the used clef
            midiNotes[](int): List of MidiNotes (output of C++)
        
        Returns:
            int: step-distance from center-line (+, -)
            int: what accidental is written (0 none, 1 sharp, -1 flat, 2 natural)
    '''
    
    #Run once
    (startIndex, used_clef, accidentals) = clefCalculation.clefCalculation(clef, key)

    
    midiDict = {}

    for midiNote in midiNotes:
        #already calculated
        if(midiNote in midiDict):
            continue

        
        ##########
        #The Calculation of the number of steps
        ###########
        acc = 0
        
        shift = 0
        x = midiNote - clef
        while(x < 0):
            shift += 1
            x += 12

        i = startIndex
        while(used_clef[i] <= x):
            i = (i+1)%5
            steps = x - i
        #when it is a note not innate to the key
        if(x == used_clef[i]):
            acc = accidentals[i]
            if(key >= 0):
                steps -= 1#look inot my memos
            
        if(midiNote < clef):
            steps = -7*shift
        ##############
        #End of Calculation
        ##############
        writeNote(midiDict[midiNote])
    return




    #ViolinSchlüssel H4 Midi 71
    #BassSchlüssel D3 Midi 50

    #midiNotes(i)-50: differenz sagt mir (theoretisch) den Abstand

def helperLines(steps):
    '''
    draws the helperlines for the note

    Params:
        steps(int): number of steps, the note takes
    
    Returns:
        null
    '''
    if(abs(int(steps/2)) < 3):
        #no helpLine necessary
        return
    
    pos = pyautogui.position()
    pyautogui.moveTo(-180, 200)#helpLine-Brush
    pyautogui.click()
    if(steps > 0):
        pyautogui.moveTo(pos.x, pos.y-14)#Bewege zurück auf oberste Linie
        v = -1
    else:
        pyautogui.moveTo(pos.x, pos.y+14)#Bewege zurück auf unterste Linie
        v = 1
    for i in range(0, abs(int(steps/2))-2):
        pyautogui.moveRel(0, v*7)
        pyautogui.click()
    pyautogui.moveTo(pos.x, pos.y)
    return



def writeNote(steps, acc):



    '''
    writes the note

    Params:
        steps(int): how many steps from the center-line
        acc(int): which accidental
    '''



    '''
    Um auf die Mittellinie des x-ten 5-Zeilensystems zu kommen:
        Hoch: y = 372+85x
        Tief: y = 354+85x
    '''
    #HelperLines (if necessary), 
    

    '''
    Welches Höhenoffset muss jeweils eingestellt werden?
        Tief:
            auf Linie x unter Mittellinie: +7*x
            zwischen Linie x und x+1 unter Mittellinie: +7*x + 4
        Hoch:
            auf Linie x über Mittellinie: -7*x
            zwischen Linie x und x+1 über Mittellinie: -7*x - 3
            -1 * (7*x + 3)
    '''
    #relative y-position:
    #Tief, notes below the middle-line
    if(steps < 0):
        y = (7 * int(steps/2) + (steps % 2) * 4)
    #Hoch, notes above the middle-line
    else:
        y = -1 * (7 * int(steps/2) + (steps % 2) * 3)


    

    #y = 372 + 85 bringt mich auf die Mittellinie eines 5-Zeilensystems.
    pyautogui.moveTo(-1645,354+85)
    pyautogui.click()
    return

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


