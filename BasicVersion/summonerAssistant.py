import pynput
import pyperclip
import os
import time
from pynput import keyboard

#constantly stores the input of the last 4 keys you pressed.
#everytime to release a key it checks to see if your last 4 keys spell out a lane assigment and summoner spell
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