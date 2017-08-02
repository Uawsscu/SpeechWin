import time
import pyttsx
engine = pyttsx.init()
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
voice = engine.getProperty('voice')
engine.setProperty('rate', 120) #Integer speech rate in words per minute.


print rate
print volume
print voice

engine.say("Hello My name is Jerry.")
engine.runAndWait()
time.sleep(3)
