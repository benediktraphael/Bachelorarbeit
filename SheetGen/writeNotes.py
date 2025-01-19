import math
from Lines import prepareSheet
from gimpfu import * # type: ignore
from processMidiNumbers import processMidiNumbers


def helperLines(steps, cur_pos, image):
    '''
    draws the helperlines for the note

    Params:
        steps(int): number of steps, the note takes
        cur_pos(int, int): coordinates (center-Line)
        image(GIMP): Current work-Image
    
    Returns:
        null
    '''
    v = -1
    if(steps < 0):
        v *= -1
    
    (x,y) = cur_pos
    drawable = image.active_layer
    pdb.gimp_context_set_brush("Hilfslinie") # type: ignore

    for i in range(0, abs(int(steps/2))-2):
        pdb.gimp_paintbrush_default(drawable, 2, [x, y+v*(48+24*(i+1))]) # type: ignore

    return



def writeSheetMusic(key, clef, midiNotes, image):

    '''
        draws all notes

        Params:
            key(int): key, the piece should be in (+: number of sharps, -: number of flats)
            clef(int): clef, the piece should be in (number of the Midi, which sits on the center line)
            midiNotes[](int, int, ??): The Piece, given from C++
            image(GIMP): ...
        Returns:
            null
    '''


    '''Preparation'''
    midiDict = {}
    processMidiNumbers(key, clef, midiNotes, midiDict)
    
    '''Important Variables'''
    '''Brushes Index: 2 * log2(Length (in Sechszehntel)) + (Tief?)'''
    brushes = ["Sechszehntel-Hoch","Sechzehntel-Tief", "Achtel-Hoch", "Achtel-Tief", "Viertel-Hoch", "Viertel-Tief", "Halbe-Hoch", "Halbe-Tief"]
    
    sign_brushes = ["x", "Vorzeichen-b", "Vorzeichen-Aufloesung", "Vorzeichen-Kreuz"]
    sign_offsets = [0, -8, 0, 0]
    x_sign_offsets = [0, -8, -32, -32]
    high_offset = 27
    low_offset = -27

    note_width = 50 #Rethink
    

    '''Starting Point'''
    x, y = 500, 548

    drawable = image.active_layer

    '''Mididict[Midinr] = [steps, sign]'''
    '''note = (length, Midinr, ???)'''

    for note in midiNotes:

        steps = midiDict[note[1]][0]
        
        brush = int(2*math.log(note[0],2) + (1 if steps < 0 else 0))

        '''Calculate y_shift'''
        y_shift = -1 * 12*steps + (high_offset if steps > 0 else low_offset)


        '''has a sign'''
        if(midiDict[note[1]][1] != 0):
            sign_brush = sign_brushes[midiDict[note[1]][1]]
            sign_offset = sign_offsets[midiDict[note[1]][1]] - 12*steps
            x_sign_offset = x_sign_offsets[midiDict[note[1]][1]]
            pdb.gimp_context_set_brush(sign_brush) # type: ignore
            pdb.gimp_paintbrush_default(drawable, 2, [x+sign_offset+x_sign_offset, y+sign_offset]) # type: ignore


        '''Select correct brush'''
        pdb.gimp_context_set_brush(brushes[brush]) # type: ignore
        
        
        '''Paint the Note and Helperlines'''
        pdb.gimp_paintbrush_default(drawable, 2, [x, y+y_shift]) # type: ignore

        if(steps > 5 or steps < -5):
            helperLines(steps, (x,y), image)
        

        '''shift on the x-axes'''
        x += int(note_width* (1.5 ** math.log(note[0], 2))) # check, what looks nice


        '''move to start of next system'''
        if(x >= 2150):
            x = 500
            y += 12*24
            if(y > 3200):
                #last system of the page is full
                return#maybe change later on?

    gimp.Display(image) # type: ignore
    return


import math
print()