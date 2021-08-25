#!/usr/bin/python

import subprocess
import os 

p = subprocess.Popen(['pgrep', '-f', '/home/pi/cam/app/cam.py'], stdout=subprocess.PIPE)
out, err = p.communicate()

if len(out.strip()) == 0:
    print("(Re)Starting cam!")
    os.system("/home/pi/cam/app/cam.py")
else:
    print("Cam already running!")
