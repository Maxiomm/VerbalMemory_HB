import pytesseract
from PIL import ImageGrab
import tempfile
import pyautogui
import os
import keyboard

# Coordonnées du screenshot
x = 558
y = 470
width = 772
height = 140

# Liste de mots
word_list = []



# Fonction pour lire un mot à partir d'un screenshot
def read_word_from_screenshot(x, y, width, height):
    # Prendre un screenshot temporaire
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_file:
        temp_filename = temp_file.name
        screenshot = ImageGrab.grab(bbox=(x, y, x+width, y+height))
        screenshot.save(temp_filename)

    # Utiliser Pytesseract pour lire le texte
    text = pytesseract.image_to_string(temp_filename)

    # Supprimer le fichier temporaire
    os.remove(temp_filename)

    return text.strip()



# Fonction pour cliquer en fonction de si le mot est nouveau ou non
def click_based_on_word(word):
    if word not in word_list:
        # Si le mot est nouveau, cliquer aux coordonnées (1040, 650)
        pyautogui.click(1040, 650)
    else:
        # Sinon, cliquer aux coordonnées (866, 650)
        pyautogui.click(866, 650)


try:
    while True:
        # Appel de la fonction pour lire le mot dans le screenshot
        word = read_word_from_screenshot(x, y, width, height)

        # Appel de la fonction pour cliquer en fonction du mot
        click_based_on_word(word)

        # Vérifier si le mot lu n'est pas déjà dans la liste, puis l'ajouter si nécessaire
        if word not in word_list:
            word_list.append(word)
            print("Liste de mots mise à jour:", word_list, "\n\n")

        # Vérifier si Ctrl+C est pressé
        if keyboard.is_pressed('ctrl+c'):
            raise KeyboardInterrupt

except KeyboardInterrupt:
    print("\nArrêt de la boucle suite à une interruption.")