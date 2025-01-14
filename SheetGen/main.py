import Lines
import writeNotes


def setCoordinates():
     
    with open("SetUp.txt", "r") as file:
        coordinates = [eval(line.strip()) for line in file]

    writeNotes.helperLineBrush = coordinates[10]
    writeNotes.brushes = [coordinates[6], coordinates[7], coordinates[2],coordinates[3], coordinates[8], coordinates[9], coordinates[4], coordinates[5]]
    writeNotes.additional_brushes = [coordinates[10], coordinates[11], coordinates[13], coordinates[12], coordinates[14]]

    Lines.clefs = [coordinates[15], coordinates[16]]
    Lines.keys = [coordinates[13], coordinates[14]]

    Lines.lineBrush = coordinates[11]

    paper_size = (coordinates[1][0]-coordinates[0][0], coordinates[1][1]-coordinates[0][1])

    effektive_paper_heigth = paper_size[1] * 0.85

    Lines.systemHeight = int(effektive_paper_heigth/25)


    Lines.lineLength = paper_size[0] * 0.85
    Lines.lineStart = (coordinates[0][0] + (paper_size[0] * 0.075), coordinates[0][1] + 0.12 * paper_size[1])

    return

setCoordinates()
Lines.prepareSheet(71, 3)