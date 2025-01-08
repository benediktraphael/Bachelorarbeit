import pyautogui
import time
#Ich erwarte eine Liste an Noten mit der Form
#(Position (in 1/16), Ton, Dauer (in 1/16)) 
#Bsp. (8, C4, 4 ):
#bedeutet: C4 wird 8/16 nach Begin (nach 2 viertel) für 4/16 (ein Viertel) gespielt.

#Da ich eine Melodie erwarte, sollte es zu keiner Überlappung kommen.


'''
Ermitteln der Positionen (Wo sind die Pinsel?)
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
    
Speicher in Array an Index
2 * log2(Länge (in Sechszehntel)) + (Tief?)  ... 2^x Sechszehntel lang
    Bsp. Achtel Hoch = 2 * 1 + 0
Wenn Pausen dazu kommen (3 * log + 0 (h) 1(tief) 2(pause))
'''


