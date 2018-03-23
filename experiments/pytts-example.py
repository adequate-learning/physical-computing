#!/usr/bin/env python
#
# pip install pyttsx3
# sudo apt install -y libespeak-dev

import pyttsx3

engine = pyttsx3.init()
engine.say("Hello World")
engine.setProperty('rate', 120)
engine.setProperty('volume', 0.5)
engine.runAndWait()
