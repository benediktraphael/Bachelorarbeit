import Lines
import writeNotes


def setCoordinates():
     
    with open("SetUp.txt", "r") as file:
        coordinates = [eval(line.strip()) for line in file]

    writeNotes.helperLineBrush = coordinates[10]
    writeNotes.brushes = [coordinates[6], coordinates[7], coordinates[2],coordinates[3], coordinates[8], coordinates[9], coordinates[4], coordinates[5]]
    writeNotes.additional_brushes = [coordinates[10], coordinates[11], coordinates[13], coordinates[12], coordinates[14]]

    Lines_clefs = [coordinates[15], coordinates[16]]
    Lines_keys = [coordinates[13], coordinates[14]]

    Lines_lineBrush = coordinates[11]

    paper_size = (coordinates[1][0]-coordinates[0][0], coordinates[1][1]-coordinates[0][1])

    effektive_paper_heigth = paper_size[1] * 0.85

    Lines_systemHeight = int(effektive_paper_heigth/25)


    Lines_lineLength = paper_size[0] * 0.85
    Lines_lineStart = (coordinates[0][0] + (paper_size[0] * 0.075), coordinates[0][1] + 0.12 * paper_size[1])


    Lines.prepareSheet(71, 0, Lines_lineBrush, Lines_lineLength, Lines_systemHeight, Lines_lineStart, Lines_clefs, Lines_keys)
    return

setCoordinates()