import sys
from tkinter import * #graphic interface
import time #do I realy need to explain ?
import pygame #to play sounds
import os, random #to get random file
from PIL import Image
import subprocess
"""import RPi.GPIO as GPIO

GPIO.setwarnings(False) #do not display the warnings
GPIO.setmode (GPIO.BCM) #or GPIO.setmode(GPIO.BOARD)

GPIO.setup(14,GPIO.IN) #GPIO 14 -> IR sensor as input"""

#functions
def close(event):
    sys.exit()

def new_cap(event):
	file = open("caps.txt","w") 
	file.write('%d' % (cap.get() + 1)) 
	file.close() 
	get_caps_amount()
	play_random_sound()
	#show_random_image()
	
def get_caps_amount():
	with open("caps.txt") as file: #with statment corresponds to c# using du
		cap.set(file.readline())

"""def check_sensor():
	while True:
		if(IO.input(14)==False): #object is near
			new_cap()
			time.sleep(1)"""
			
def play_random_sound():
	pygame.mixer.init()
	pygame.mixer.music.load('sounds\\' + get_random_sound())
	pygame.mixer.music.play()

def get_random_sound():
	return random.choice(os.listdir("sounds\\"))
	
def show_random_image():
	test_image=PhotoImage(file = "testbg.png")
	background_label.configure(image=test_image)
	background_label.image=test_image
	"""background_image=PhotoImage(file = "testbg.png")
	background_label.configure(image=background_image)
	background_label.image=background_image"""
	
	
#create window
window = Tk()

#initiate variables
cap = IntVar()
get_caps_amount()

#window properties
window.geometry("1280x1024") #Bob size
#window.attributes('-fullscreen', True)
window.overrideredirect(1) #Remove border

background_image=PhotoImage(file = "bobbg.png")
background_label = Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#add number of caps
label_caps = Label(window, textvariable=cap, font=("Arial",400), bg='black', fg='#ffe5cc')
label_caps.pack(expand=YES)
frame_caps = Frame(window)
frame_caps.pack()

#events
window.bind('<Escape>', close)
window.bind('<Insert>', new_cap)

#prepare functons out of window.mainloop()
#root.after(0, check_sensor)# check_sensor will run as soon as the mainloop starts

#display window
window.mainloop()