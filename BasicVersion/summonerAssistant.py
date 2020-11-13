import pynput
import pyperclip
import os
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput import keyboard

#get summoner name
summonername = input("please enter your summoner name: ")
my_url = 'https://na.op.gg/summoner/userName=' + summonername

#opens chrome window controlled by bot
PATH = os.getcwd() + "/chromedriver"
driver = webdriver.Chrome(PATH)

spelltime = [2]
def get_info(lane):
	driver.get(my_url)
	link = driver.find_element_by_link_text("Live Game")
	link.click()
	time.sleep(1)
	gametime = driver.find_element_by_class_name("Time")
	spelltime = gametime.text.split(":")
	spelltime[0] = str(int(spelltime[0]) + 5)
	pyperclip.copy(lane + " flash " + spelltime[0] + ":" + spelltime[1])

#constantly stores the input of the last 4 keys you pressed.
#everytime to release a key it checks to see if your last 4 keys spell out a lane assigment and summoner spell
keys = ["a", "b", "c", "d"]
count = 0
while True:
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
			get_info("top")
	if "'j'" in keys and "'u'" in keys and "'n'" in keys:
		if "'f'" in keys:
			get_info("jungle")
	if "'m'" in keys and "'i'" in keys and "'d'" in keys:
		if "'f'" in keys:
			get_info("mid")
	if "'a'" in keys and "'d'" in keys and "'c'" in keys:
		if "'f'" in keys:
			get_info("adc")
	if "'s'" in keys and "'u'" in keys and "'p'" in keys:
		if "'f'" in keys:
			get_info("support")