import math
import pyautogui
import time
#from clefCalculation import clefCalculation 


def clefCalculation(clef, key):
    '''
        determines the calculation-array

        Args:
            key(int): number of accidentals (+ sharp, - flat); example: G major = +1
            clef(int): MidiNumber of the note, which is on the center-line in the used clef
        
        Returns:
            [](int): relative positions of Midis, which have accidentals
            (int): The StartIndex, which black key is the next.
            (int(bool)): natural or standard sign.(0 none, 1 sharp, -1 flat, 2 natural)

    '''
    #Steps from F to the black Notes in Order (Fis, Gis, Ais, Cis, Dis)
    used_clef = [1,3,5,8,10]
    #The movement, such it is relative to Center-Tone and not F.
    match clef: 
        case 71:#Treble
            used_clef = [(a - 6) % 12 for a in used_clef]
            startIndex = 3#Cis is the first accidental from H
        case 50:#Bass
            used_clef = [(a + 5) % 12 for a in used_clef]
            startIndex = 4#Dis is the first accidental from D


    #Order, in which sharps, flats effect them (1. Fis, 2. Cis, ...)
    accidentals_order = [0,3,1,4,2]

    #if there is an key, the changed white key needs a natural sign.
    #0 means, standard sign. 1 means Changed, natural sign
    accidentals = [0, 0, 0, 0, 0]


    #flats, as means that a (one above) is now the outlieer
    while(key < 0):
        used_clef[accidentals_order[key]] += 1
        key += 1
        accidentals[accidentals_order[key]] = 1

    while(key > 0):
        used_clef[accidentals_order[key-1]] -= 1
        key -= 1
        accidentals[accidentals_order[key-1]] = 1

    return (startIndex, used_clef, accidentals)

#Ich erwarte eine Liste an Noten mit der Form
#(Position (in 1/16), Ton(ohne Vorzeichen), Vorzeichen(null, b, #), Dauer (in 1/16)) 
#Bsp. (8, C4, null, 4 ):
#bedeutet: C4 wird 8/16 nach Begin (nach 2 viertel) für 4/16 (ein Viertel) gespielt.

#Da ich eine Melodie erwarte, sollte es zu keiner Überlappung kommen.

#pyautogui.moveTo(-1645,364)




    #while clef(startIndex+i < Steps): i++
    #Steps - (startIndex+i)%5

    #these show the Order, in which the accidentals are changed. for Treble

midiNotes = [(4, 60, 0), (4, 62, 0), (4, 64, 0), (4, 65, 0), (4, 67, 0), (4, 69, 0), (4, 71, 0), (4, 72, 0)]


def processMidiNumbers(key, clef, midiNotes, midiDict):
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
    (startIndex, used_clef, accidentals) = clefCalculation(clef, key)


    for _,midiNote, _ in midiNotes:
        #already calculated
        if(midiNote in midiDict):
            continue

        
        ##########
        #The Calculation of the number of steps
        ###########
        acc = 0
        steps = 0
        shift = 0
        x = midiNote - clef
        while(x < 0):
            shift += 1
            x += 12

        i = startIndex
        while(used_clef[i] <= x):
            i = (i+1)%5
        
        steps = x - (i-startIndex)%5
        #when it is a note not innate to the key
        if(x == used_clef[i]):
            acc = accidentals[i]
            if(key >= 0):
                steps -= 1#look inot my memos
            
        if(midiNote < clef):
            steps -= 7*shift
        ##############
        #End of Calculation
        ##############
        midiDict[midiNote] = (steps, acc)
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

def writeSheetMusic(key, clef, midiNotes):

    #constant how much do I move to the right for a 1/16th
    #for 1/4 I move 4*width
    note_width = 5


    brushes = [(-150, 175), (-115, 175), (-115, 140), (-80, 140), (-80, 175), (-45, 175), (-45, 140), (-180, 175)]

    '''
    Zusatz
    Hilfslinie (-180, 200)
    Pinsel (-150, 200)
    Vorzeichen
    ...
    Pausen
    ...
    '''
    additional_brushes = [(-180, 200), (-150, 200)]


    #preperation
    midiDict = {}
    processMidiNumbers(key, clef, midiNotes, midiDict)
    #counts, how many width are left in this system
    counter = 200
    current_brush = -1
    for note in midiNotes:
        '''2 * log2(Länge (in Sechszehntel)) + (Tief?)'''
        steps = midiDict[note[1]][0]
        brush = int(2*math.log2(note[0]) + (1 if steps < 0 else 0))#Punktierte Noten fehlen noch

        #select right brush
        ''' if(brush != current_brush):
            current_brush = brush
            pos = pyautogui.position()
            pyautogui.moveTo(brushes[brush])
            pyautogui.click()
            pyautogui.moveTo(pos)'''
        
        if(steps < 0):
            y = -1 * (7 * int(steps/2) - (steps % 2) * 4)#da steps negativ
        #Hoch, notes above the middle-line
        else:
            y = -1 * (7 * int(steps/2) + (steps % 2) * 3)
        
        pyautogui.moveRel(0, y)
        pyautogui.click()
        #move back and to next position
        pyautogui.moveRel(10, -y)#note[0]*note_width
        '''
        Um auf die Mittellinie des x-ten 5-Zeilensystems zu kommen:
            Hoch: y = 372+85x
            Tief: y = 355+85x
        '''
        counter -= note[0]
        if(counter <= 0):
            #move to next system
            pyautogui.moveRel(-1*(abs(counter) + 20)*note_width, 85)
            



    #Ich mache alle helperlines am ende
    

    return
pyautogui.moveTo(-1500, 355+85)
writeSheetMusic(0, 71, midiNotes)


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


