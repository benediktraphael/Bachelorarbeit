from gimpfu import * # type: ignore

def createImage():
    width = 2480
    height = 3508

    new_image = gimp.Image(width, height, GRAY) # type: ignore
    background = gimp.Layer(new_image, "Hintergrund", width, height, GRAY_IMAGE, 100, NORMAL_MODE) # type: ignore
    background.fill(WHITE_FILL) # type: ignore
    new_image.add_layer(background)
    return new_image


def drawLines(image):
    drawable = image.active_layer
    
    #Select Brush
    pdb.gimp_context_set_brush("Noten-Linien") # type: ignore
    pdb.gimp_context_set_foreground((0, 0, 0)) # type: ignore
    
    pdb.gimp_context_set_brush_size(5) # type: ignore
    #Test how it looks
    x = 250
    y = 500

    for j in range(10):
        for i in range(5):
            pdb.gimp_paintbrush_default(drawable, 4, [x,y, 2250, y]) # type: ignore
            y += 24
        y += 7*24
    return

def drawClefs(image, clef):
    drawable = image.active_layer
    x = 300
    y = 548

    #need to check for offsets
    if(clef == 71):
        offset = 12
        pdb.gimp_context_set_brush("Schluessel_Violin") # type: ignore
    if(clef == 50):
        offset = -8
        pdb.gimp_context_set_brush("Schluessel_Bass") # type: ignore
    
    for j in range(10):
        pdb.gimp_paintbrush_default(drawable, 2, [x, y+offset]) # type: ignore
        y += 12*24
    return


def drawKey(image, key, clef):

    drawable = image.active_layer
    accidentals_order = [0,3,1,4,2]
    used_clef = [1,3,5,8,10]
    
    sharps = [-48, -12, -60, -24, 12, -36, 0]
    flats = [0,36, -12, 24, -24, 12, -36]
    

    if(key < 0):
        pdb.gimp_context_set_brush("Vorzeichen-b") # type: ignore
        used_acc = flats
        offset = -8
        width = 10
    else:
        pdb.gimp_context_set_brush("Vorzeichen-Kreuz") # type: ignore
        used_acc = sharps
        offset = 0
        width = 30

    if(clef == 50):
        used_acc = [x + 24 for x in used_acc]

    y = 548

    for j in range(10):
        x = 350
        for i in range(0, key, (-1 if key < 0 else 1)):
           pdb.gimp_paintbrush_default(drawable, 2, [x, y+used_acc[i]+offset]) # type: ignore
           x += width + 10

        y += 12*24
    return


def prepareSheet(clef, key):
    image = createImage()
    drawLines(image)
    drawClefs(image, clef)
    drawKey(image, key, clef)
    gimp.Display(image) # type: ignore
    return image