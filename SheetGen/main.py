import Lines
import writeNotes
import time
import pyautogui


#2480x3508 px soll das Papier sein.





midiNotes = [(4, 72, 0), (4, 74, 0), (4, 76, 0), (4, 77, 0), (4, 79, 0), (4, 81, 0), (4, 83, 0), (4, 84, 0)]
def setCoordinates():
     
    with open("SetUp.txt", "r") as file:
        coordinates = [eval(line.strip()) for line in file]

    writeNotes_helperLineBrush = coordinates[10]
    writeNotes_brushes = [coordinates[6], coordinates[7], coordinates[2],coordinates[3], coordinates[8], coordinates[9], coordinates[4], coordinates[5]]
    writeNotes_additional_brushes = [coordinates[10], coordinates[11], coordinates[13], coordinates[12], coordinates[14]]

    Lines_clefs = [coordinates[15], coordinates[16]]
    Lines_keys = [coordinates[13], coordinates[14]]

    Lines_lineBrush = coordinates[11]

    paper_size = (coordinates[1][0]-coordinates[0][0], coordinates[1][1]-coordinates[0][1])

    effektive_paper_heigth = paper_size[1] * 0.85

    Lines_systemHeight = int(effektive_paper_heigth/25)


    Lines_lineLength = paper_size[0] * 0.85
    Lines_lineStart = (coordinates[0][0] + (paper_size[0] * 0.075), coordinates[0][1] + 0.12 * paper_size[1])


    writeNotes_startPos = (Lines_lineStart[0]+ (paper_size[0] * 0.075), Lines_lineStart[1] + (2 * Lines_systemHeight / 5))

    Lines.prepareSheet(71, 0, Lines_lineBrush, Lines_lineLength, Lines_systemHeight, Lines_lineStart, Lines_clefs, Lines_keys)
    writeNotes.writeSheetMusic(0, 71, midiNotes, writeNotes_brushes,writeNotes_additional_brushes, writeNotes_startPos, (Lines_systemHeight/5))
    return

#setCoordinates()
time.sleep(5)
pyautogui.click()
pyautogui.moveRel(1,1)
pyautogui.click()
pyautogui.moveRel(1,1)
pyautogui.click()
pyautogui.moveRel(1,1)
pyautogui.click()