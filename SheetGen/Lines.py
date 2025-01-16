from gimpfu import *

def createImage():
    width = 2480
    height = 3508

    new_image = gimp.Image(width, height, GRAY)
    background = gimp.Layer(new_image, "Hintergrund", width, height, GRAY_IMAGE, 100, NORMAL_MODE)
    background.fill(WHITE_FILL)
    new_image.add_layer(background)
    gimp.Display(new_image)
    gimp.displays_flush()
    return new_image


def drawLines(image):
    drawable = image.active_layer
    #Select Brush
    pdb.gimp_context_set_brush("Noten-Linien")

    #Test how it looks
    x = 250
    y = 500

    for j in range(10):
        for i in range(5):
            pdb.gimp_paintbrush_default(drawable, 4, [x,y, 2250, y])
            y += 24
        y += 7*24
    return

def drawClefs(image, clef):
    drawable = image.active_layer
    x = 300
    y = 548

    #need to check for offsets
    if(clef == 71):
        offset = 0
        pdb.gimp_context_set_brush("Zusatz-zSchluessel_Violin")
    if(clef == 50):
        offset = 0
        pdb.gimp_context_set_brush("Zusatz-zSchluessel_Bass")
    
    for j in range(10):
        pdb.gimp_paintbrush_default(drawable, 2, [x, y])
        y += 12*24
    return


def drawKey(image, key):

    drawable = image.active_layer
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
    image = createImage()
    drawLines(image)
    drawClefs(image, clef)
    drawKey(image, key)
    return