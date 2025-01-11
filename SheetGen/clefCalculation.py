
def clefCalculation(clef, key):
    '''
        determines the calculation-array

        Args:
            key(int): number of accidentals (+ sharp, - flat); example: G major = +1
            clef(int): MidiNumber of the note, which is on the center-line in the used clef
        
        Returns:
            [5](int): relative positions of Midis, which have accidentals
            (int): The StartIndex, which black key is the next.
            [5](int): which accidental for which midi 2: natural, 3: sharp, 1: flat 
    '''


    '''midiSteps from F to the black Notes in Order (Fis, Gis, Ais, Cis, Dis)'''
    used_clef = [1,3,5,8,10]

    '''Shift, such relative to center-Midi of clef
        startIndex shows, which accidental is on the closest right of the new center-Midi'''
    match clef: 
        case 71:#Treble
            used_clef = [(a - 6) % 12 for a in used_clef]
            startIndex = 3
        case 50:#Bass
            used_clef = [(a + 3) % 12 for a in used_clef]
            startIndex = 4


    '''Order, in which sharps, flats effect them (1. Fis, 2. Cis, ...)(backwards for flats)'''
    accidentals_order = [0,3,1,4,2]

    '''what accidental does a midi get, if it is in used_clef?'''
    '''2: natural, 3: sharp, 1: flat'''
    accidentals = [3,3,3,3,3]
    if(key < 0):
        accidentals -= 2


    '''In G-Major (key = 1): F# is the normal midi and F is the outlier, which needs special representation'''

    '''flats: represented like midi+1 (Ab looks like A)'''
    while(key < 0):
        used_clef[accidentals_order[key]] += 1
        key += 1
        accidentals[accidentals_order[key]] = 2

    '''sharps: represented like midi-1 (G# looks like G)'''
    while(key > 0):
        used_clef[accidentals_order[key-1]] -= 1
        key -= 1
        accidentals[accidentals_order[key-1]] = 2


    return (startIndex, used_clef, accidentals)
