from gtts import gTTS
import os

# Text = input("Enter the text: \n")
with open('text.txt') as f:
    Text = f.read().replace("\n", " ")

language = 'en'

output = gTTS(text = Text, lang = language, slow = False)

output.save("taudio.mp3")

os.system("start taudio.mp3")

