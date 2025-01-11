import math
import pyautogui
import time
from Lines import prepareSheet
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

    '''MidiNotes: length, MidiNumber'''


    '''Preparation'''
    midiDict = {}
    processMidiNumbers(key, clef, midiNotes, midiDict)
    

    '''Positions of brushes'''
    brushes = [(-150, 175), (-115, 175), (-115, 140), (-80, 140), (-80, 175), (-45, 175), (-45, 140), (-180, 175)]
    additional_brushes = [(-180, 200), (-150, 200),(-80, 200),(-115,200),(-45, 200)]

    #in additional brushes 1, 2, 3 from signs_index are the accidentals (b, natural sharp)
    signs_index = 1

    '''needed offset = 2*(accidental(b, natural, sharp)-1) + (steps < 0?)*1 RETHINK'''
    signs_offsets = [-10, 7, -10, 10, -8, 10]

#abstand x+10 ist gut
#auflösen, hoch y-10 ist gut
#auflösen, tief y+10 ist gut
#b, tief y+7 ist gut
#b hoch y-10 ist gut
#KReuz hoch y-8 ist gut
#Kreuz tief, y+10 ist gut
   # B(-80, 200)
# Auflösung(-115,200)
  #  Kreuz(-45, 200)
  #  Pausen



    '''constant x-shift per 1/16 and number of 1/16 per System'''
    note_width = 15
    counter = 200
    
    '''
    Wann liegen Hoch Tief auf der Mittellinie (x, 364)?
        pyautogui.moveTo(x, 373) dann ist Hoch mittig
        pyautogui.moveTo(x, 355) dann ist Tief mittig

    Ergo:
        Hoch-Offset: 9
        Tief-Offset: -9
    '''
    high_offset = 9
    low_offset = -9

    '''bring mouse in the right position'''
    pyautogui.moveTo(-1500, 364+85*1)

    for note in midiNotes:

        steps = midiDict[note[1]][0]
        '''Brushes Index: 2 * log2(Länge (in Sechszehntel)) + (Tief?)'''
        brush = int(2*math.log2(note[0]) + (1 if steps < 0 else 0))#Punktierte Noten fehlen noch


        '''Calculate y-shift'''
        if(steps < 0):
            y = -1 * (7 * int(steps/2) - (steps % 2) * 4)+low_offset

        else:
            y = -1 * (7 * int(steps/2) + (steps % 2) * 3)+high_offset


        '''has a sign'''
        if(midiDict[note[1]][1] != 0):
            '''select correct sign'''
            cur_pos = pyautogui.position()
            pyautogui.moveTo(additional_brushes[signs_index+midiDict[note[1]][1]])
            pyautogui.click()
            pyautogui.moveTo(cur_pos)
            '''needed offset = 2*(accidental(b, natural, sharp)-1) + (steps < 0?)*1'''
            sign_offset_index = 2 * (midiDict[note[1]][1]-1) + (1 if steps < 0 else 0)
            sign_offset = signs_offsets[sign_offset_index]
            pyautogui.moveRel(0, y+sign_offset)
            pyautogui.click()
            pyautogui.moveRel(10, -(y+sign_offset))

        '''Select correct brush''' 
        cur_pos = pyautogui.position()
        pyautogui.moveTo(brushes[brush])
        pyautogui.click()
        pyautogui.moveTo(cur_pos)
        
        
        '''Paint the Note and Helperlines'''
        pyautogui.moveRel(0, y)
        pyautogui.click()
        pyautogui.moveRel(0, -y)
        if(abs(int(steps/2)) > 2):
            helperLines(steps)
        

        '''shift on the x-axes'''
        x_shift = (1.5 ** int(math.log2(note[0])))*note_width #Experimenting on what looks nice
        pyautogui.moveRel(x_shift, 0)
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
prepareSheet(71)
time.sleep(3)
midiNotes = [(4, 60, 0), (4, 61, 0), (8, 64, 0), (4, 65, 0), (2, 67, 0), (2, 69, 0), (1, 71, 0), (1, 72, 0)]
writeSheetMusic(0, 71, midiNotes)

'''
Ich erwarte eine Liste an Noten mit der Form
    (Dauer (in Sechszehntel), MidiNummber, ???)
    Bsp. (4, Midi(C4), ???): C4 wird für 4/16 (ein Viertel) gespielt.

Da ich eine Melodie erwarte, sollte es zu keiner Überlappung kommen.


Pinselpositionen
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
    2 * log2(Länge (in Sechszehntel)) + 1 * (istTief?)
    Bsp. Achtel Hoch = 2 * log2(2) + 0


Wenn Pausen dazu kommen (3 * log + 0 (h) 1(tief) 2(pause))?#Idee
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
'''