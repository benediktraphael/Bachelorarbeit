from gimpfu import *

def drawLines():
    #Select Brush
    pdb.gimp_context_set_brush("Zeilen-Pinsel")

    #Test how it looks
    x = 250
    y = 500

    for j in range(10):
        for i in range(5):
            pdb.gimp_paintbrush_default(drawable, 4, [x,y, 2250, y])
            y += 24
        y += 7*24
    return

def drawClefs(clef):

    x = 300
    y = 548

    #need to check for offsets
    match clef:
        case 71:
            offset = 0
            pdb.gimp_context_set_brush("Zusatz-zSchlüssel_Violin")
        case 50:
            offset = 0
            pdb.gimp_context_set_brush("Zusatz-zSchlüssel_Bass")
    
    for j in range(10):
        pdb.gimp_paintbrush_default(drawable, 2, [x, y])
        y += 12*24
    return


def drawKey(key):
    accidentals_order = [0,3,1,4,2]
    used_clef = [1,3,5,8,10]
    

    sharps = [-14, -4, -18, -7, 4]#Ausmessen
    flats = [-2, -20,-9,1,-13]#Ausmessen
    
    if(key < 0):
        pdb.gimp_context_set_brush("Zusatz-Vorzeichen-b")
        used_acc = flats
    else:
        pdb.gimp_context_set_brush("Zusatz-Vorzeichen-Kreuz")
        used_acc = sharps

    x = 350
    y = 548

    for j in range(10):

        for i in range(0, key, (-1 if key < 0 else 1)):
           pdb.gimp_paintbrush_default(drawable, 2, [x, y+used_acc[i]])
        
        y += 12*24
    return


def prepareSheet(clef, key):
    drawLines()
    drawClefs(clef)
    drawKey(key)
    return


