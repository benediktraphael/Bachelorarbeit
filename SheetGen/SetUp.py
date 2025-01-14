from pynput import mouse
import pyautogui
standart_Message = "Klicken Sie bitte auf "

messages = [
    "die Ecke (links-oben) von dem Din-A4-Blatt",
    "die Ecke (rechts-unten) von dem Din-A4-Blatt",
    "die Achtel (Kopf oben)",
    "die Achtel (Kopf unten)",
    "die Halbe (Kopf oben)",
    "die Halbe (Kopf unten)",
    "die Sechszehntel (Kopf oben)",
    "die Sechszehntel (Kopf unten)",
    "die Viertel (Kopf oben)",
    "die Viertel (Kopf unten)",
    "die Hilfslinie (der Horizontale Pinsel)",
    "den Punkt-Pinsel",
    "das Auflösungszeichen",
    "das b",
    "das Kreuz",
    "den Bass-Schlüssel",
    "den Violin-Schlüssel"
    ]

click_positions = []

click_count = 1


def on_click(x, y, button, pressed):

    global click_count, click_positions

    if pressed:
        click_positions.append((pyautogui.position().x, pyautogui.position().y))
        if(click_count >= len(messages)):
            return False

        print(standart_Message, messages[click_count])
        click_count += 1


def setUp():
    global click_count, click_positions
    click_count = 1
    click_positions.clear() 

    print(standart_Message, messages[0])

    with mouse.Listener(on_click=on_click) as listener:
       listener.join()

    print("Done")
    print(click_positions)

    with open("SetUp.txt", "w") as file:
        for i in range(0, len(click_positions)):
            file.write(str(click_positions[i]) + "\n")
    return
setUp()