#!/usr/bin/python3
from dotenv import dotenv_values
from gpiozero import Button, LED
from time import sleep
import datetime, dropbox, picamera, os

config = dotenv_values(".env")
db_ac = config["DB_ACCESS_TOKEN"]

db = dropbox.Dropbox(db_ac)

button = Button(7, pull_up=False)
led = LED(14)

def pressed():
    print("button was pressed")
    led.on()
    
    # Foto erstellen und lokal speichern
    camera = picamera.PiCamera()
    camera.vflip = True
    #camera.resolution=(1280, 960)
    camera.resolution=(2592, 1944)
    print("Taking pictures")
    for x in range(5):
        localname = 'tmp' + str(x) + '.jpg'
        camera.capture(localname)
        #sleep(1)
    camera.close()
    print("Pictures created")

    # Foto hochladen
    for x in range(5):
        localname = 'tmp' + str(x) + '.jpg'
        f = open(localname, 'rb')
        timestamp = datetime.datetime.now().isoformat()
        upname = '/rapi-' + timestamp + '.jpg'
        db.files_upload(f.read(), upname)
        f.close()
        os.remove(localname)

def released():
    print("button was released")
    led.off()

button.when_pressed = pressed
button.when_released = released

print("cam is ready")

while True:
    pass

