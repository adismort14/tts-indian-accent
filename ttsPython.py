import pyttsx3
import sys

engine = pyttsx3.init()  # object creation

rate = engine.getProperty("rate")  # getting details of current speaking rate
engine.setProperty("rate", 150)  # setting up new voice rate
rate = engine.getProperty("rate")  # getting details of current speaking rate

volume = engine.getProperty(
    "volume"
)  # getting to know current volume level (min=0 and max=1)
engine.setProperty("volume", 1.0)

voices = engine.getProperty("voices")
for voice in voices:
    print(voice)
engine.setProperty("voice", voices[1].id)

text = " ".join(sys.argv[1:])

engine.say(text)
engine.runAndWait()
engine.stop()
