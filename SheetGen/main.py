#! /usr/bin/env python2
from ReadFile import Read
from Lines import prepareSheet
from writeNotes import writeSheetMusic

def main():
    
    print("Guten Tag...")
    print("Nennen Sie bitte den Dateinamen von der Datei, die realisiert werden soll...\n")
    filename = raw_input()
    midiNotes = Read(filename)
    print("In welchem Notenschluessel soll das Stueck realisiert werden? \n 71: Violinschluessel \n 50: Bassschluessel \n")
    clef_string = (raw_input())
    print("In welcher Tonart soll das Stueck realisiert werden?\n Anzahl Kreuze \n oder -1 * Anzahl b's\n")
    key_string = (raw_input())


    clef = int(clef_string)
    key = int(key_string)

    print("Vielen Dank, Ich werde jetzt starten...")
    
    print("Notenblatt vorbereiten...")
    image = prepareSheet(clef, key)
    print("Notenblatt vorbereitet!\n")
    

    print("Verarbeitung der Noten...")
    writeSheetMusic(key, clef, midiNotes, image)
    print("Notenverarbeitung Abgeschlossen!")

    print("Auf Wiedersehen!")
    return

