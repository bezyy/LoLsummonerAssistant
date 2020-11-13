import pynput
import pyperclip
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
from pynput import keyboard

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

#determines which mode user wants to use
mode = input("Enter 0 for voiceRecognition mode OR enter 1 for textRecognition mode: ")

# this while loop makes it so the program is constantly listening
# here it searches for specific key words like the lane and type of spell
while int(mode) == 0:
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
			speak

keys = ["a", "b", "c", "d"]
count = 0
while int(mode) == 1:
	def on_press(key):
		global keys, count
		if count < 4:
			del keys[int(count)]
			keys.insert(int(count), str(key))
			count += 1
		else:
			count = 0
			del keys[int(count)]
			keys.insert(int(count), str(key))
			count += 1

	def on_release(key):
		return False
	
	with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
		listener.join()

	if "'t'" in keys and "'o'" in keys and "'p'" in keys:
		if "'f'" in keys:
			pyperclip.copy("champnameTOP flash time")
	if "'j'" in keys and "'u'" in keys and "'n'" in keys:
		if "'f'" in keys:
			pyperclip.copy("champnameJungle flash time")
	if "'m'" in keys and "'i'" in keys and "'d'" in keys:
		if "'f'" in keys:
			pyperclip.copy("champnameMID flash time")
	if "'a'" in keys and "'d'" in keys and "'c'" in keys:
		if "'f'" in keys:
			pyperclip.copy("champnameADC flash time")
	if "'s'" in keys and "'u'" in keys and "'p'" in keys:
		if "'f'" in keys:
			pyperclip.copy("champnameSUP flash time")
