import pyperclip
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

# says "done" when summoner spell timer is copied to clipboard
def speak():
	filename = "voice.mp3"
	playsound.playsound(filename)

#listens to your microphone and returns text for what you said
def get_audio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
		said = ""

		try:
			said = r.recognize_google(audio)
		except Exception as e:
			print("Exception" + str(e))

	return said

# this while loop makes it so the program is constantly listening
# here it searches for specific key words like the lane and type of spell
while True:
	text = get_audio()

	if "top" in text:
		if "flash" in text or "Flash" in text or "/" in text:
			pyperclip.copy("champnameTOP flash time")
			speak()
		if "heal" in text or "Heal" in text:
			pyperclip.copy("champnameTOP heal time")
			speak()
		if "teleport" in text or "Teleport" in text:
			pyperclip.copy("champnameTOP teleport time")
			speak()
		if "barrier" in text or "Barrier" in text:
			pyperclip.copy("champnameTOP barrier time")
			speak()

	if "mid" in text or "middle" in text:
		if "flash" in text or "Flash" in text or "/" in text:
			pyperclip.copy("champnamemid flash time")
			speak()
		if "heal" in text or "Heal" in text:
			pyperclip.copy("champnamemid heal time")
			speak()
		if "teleport" in text or "Teleport" in text:
			pyperclip.copy("champnamemid teleport time")
			speak()
		if "barrier" in text or "Barrier" in text:
			pyperclip.copy("champnamemid barrier time")
			speak()

	if "jungle" in text:
		if "flash" in text or "Flash" in text or "/" in text:
			pyperclip.copy("champnamejungle flash time")
			speak()
		if "heal" in text or "Heal" in text:
			pyperclip.copy("champnamejungle heal time")
			speak()
		if "teleport" in text or "Teleport" in text:
			pyperclip.copy("champnamejungle teleport time")
			speak()
		if "barrier" in text or "Barrier" in text:
			pyperclip.copy("champnamejungle barrier time")
			speak()

	if "80" in text or "carry" in text:
		if "flash" in text or "Flash" in text or "/" in text:
			pyperclip.copy("champnameadc flash time")
			speak()
		if "heal" in text or "Heal" in text:
			pyperclip.copy("champnameadc heal time")
			speak()
		if "teleport" in text or "Teleport" in text:
			pyperclip.copy("champnameadc teleport time")
			speak()
		if "barrier" in text or "Barrier" in text:
			pyperclip.copy("champnameadc barrier time")
			speak()

	if "support" in text:
		if "flash" in text or "Flash" in text or "/" in text:
			pyperclip.copy("champnamesupport flash time")
			speak()
		if "heal" in text or "Heal" in text:
			pyperclip.copy("champnamesupport heal time")
			speak()
		if "teleport" in text or "Teleport" in text:
			pyperclip.copy("champnamesupport teleport time")
			speak()
		if "barrier" in text or "Barrier" in text:
			pyperclip.copy("champnamesupport barrier time")
			speak()
