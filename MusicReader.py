import librosa
import numpy as np
import os

def audio_to_samples(filename):

    script_dir = os.path.dirname(os.path.abspath(__file__)) 

    audio_file = os.path.join(script_dir, "Projects/" + filename + ".mp3")
    sample_file = os.path.join(script_dir, "Projects/" + filename + ".txt")

    try:
        y, sr = librosa.load(audio_file, sr=None)

        if len(y.shape) > 1:
            y = librosa.to_mono(y)

        np.savetxt(sample_file, y, fmt="%f")

    except Exception as e:
        print(f"❌ Fehler beim Verarbeiten der Datei: {e}")


def main():
    filename = input("Welche MP3-Datei in Projects soll in Samples aufgeteilt werden?\n")
    audio_to_samples(filename)
    return

main()