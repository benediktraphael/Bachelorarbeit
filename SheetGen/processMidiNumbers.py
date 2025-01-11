from clefCalculation import clefCalculation

def processMidiNumbers(key, clef, midiNotes, midiDict):
    '''
        determines steps of occuring midiNumbers

        Args:
            key(int): number of accidentals (+ sharp, - flat); example: G major = +1
            clef(int): MidiNumber of the note, which is on the center-line in the used clef
            midiNotes[](int): List of MidiNotes (output of C++)
        
        Returns:
            int: step-distance from center-line (+, -)
            int: what accidental is written (0 none, 1 sharp, -1 flat, 2 natural)
    '''
    
    '''Preperation'''
    (startIndex, used_clef, accidentals) = clefCalculation(clef, key)


    for _,midiNote, _ in midiNotes:

        #already calculated
        if(midiNote in midiDict):
            continue

        
        ##########
        #The Calculation of steps
        ###########
        acc = 0
        steps = 0
        shift = 0
        x = midiNote - clef

        #octave, until max one octave from center
        while(x < 0):
            shift += 1
            x += 12
        while(x > 11):
            shift -= 1
            x -= 12

        #how many not innate midis are passed
        i = startIndex
        if(max(used_clef) <= x):
            i -= 1
        else:
            while(used_clef[i] < (x % 12)):
                i = (i+1)%5
        
        steps = x - (i-startIndex)%5


        #midiNote is not innate and needs a accidental
        if(x == used_clef[i]):
            acc = accidentals[i]
            #if it is a sharp, (look at piano)
            if(key >= 0):
                steps -= 1
            
        #octave back
        steps -= 7*shift


        ##############
        #End of Calculation
        ##############

        midiDict[midiNote] = (steps, acc)
    return
