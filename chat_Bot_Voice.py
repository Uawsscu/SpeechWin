from os import environ, path
import pyaudio
import sys
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *
import time
import random
from espeak import espeak
espeak.set_parameter(espeak.Parameter.Pitch, 60)
espeak.set_parameter(espeak.Parameter.Rate, 110)
espeak.set_parameter(espeak.Parameter.Range, 600)
espeak.synth("Hey Guys")
time.sleep(5)
#----------->>>>------CHAT BOT------<<<<------------#
def chatbot(H):
    # incoming and outgoing static response
    qName = ["what is your name", "who are you", "whats your name"]
    aName = ["i am called Jerry", "my name is Jerry"]
    qGreeting = ["hi", "hi there", "hello", "hello jerry", "what's up"]
    aGreeting = ["greetings", "hi", "hi there", "hello"]
    qCommon1 = ["how are you", "how are you doing"]
    aCommon1 = ["I am doing alright", "I am fine", "do ing great, and you?", "great", "pretty good", "okay"]
    qCommon2 = ["how was your day", "hows your day"]
    aCommon2 = ["it was great", "just fine"]
    qOnline = ["look for"]
    interEro = ["no internet", "i can't go online", "connection is not available", "check internet connection", "check",
                "internet", "first", "no connection", "sorry internet is not available"]
    try:
        if H == "":
            print(":~# sorry can't get it")
            # fire up internet function    #
        if H in qName:
            Ans = random.choice(aName)
        elif H in qGreeting:
            Ans = random.choice(aGreeting)
        elif H in qCommon1:
            Ans = random.choice(aCommon1)
        elif H in qCommon2:
            Ans = random.choice(aCommon2)
        else:
            print(":~# ????")
            pass
        print(":~# " + Ans)
        espeak.synth(Ans)
    except Exception:
        pass


#----->>>>----SPEECH TO TEXT-----<<<<-------

MODELDIR = "/home/uawsscu/speech_recognition/pocketsphinx/model"
DATADIR = "/home/uawsscu/speech_recognition/pocketsphinx/test/data"

config = Decoder.default_config()
config.set_string('-hmm', path.join(MODELDIR, 'en-us/en-us'))
config.set_string('-lm', path.join(MODELDIR, 'en-us/en-us.lm.bin'))
config.set_string('-dict', path.join(MODELDIR, 'en-us/cmudict-en-us.dict'))
decoder = Decoder(config)

# Switch to JSGF grammar
jsgf = Jsgf(path.join(DATADIR, 'goforward.gram'))
rule = jsgf.get_rule('goforward.move')
fsg = jsgf.build_fsg(rule, decoder.get_logmath(), 7.5)
fsg.writefile('goforward.fsg')

decoder.set_fsg("goforward", fsg)
decoder.set_search("goforward")

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
stream.start_stream()

in_speech_bf = False
decoder.start_utt()

while True:
    buf = stream.read(1024)
    if buf:
        decoder.process_raw(buf, False, False)
        if decoder.get_in_speech():
            sys.stdout.write('.')
            sys.stdout.flush()
        if decoder.get_in_speech() != in_speech_bf:
            in_speech_bf = decoder.get_in_speech()
            if not in_speech_bf:
                decoder.end_utt()
                try:
                    if decoder.hyp().hypstr != '':
                        TextToChatbot = decoder.hyp().hypstr
                        print 'Stream decoding result:', TextToChatbot
                        chatbot(TextToChatbot)
                except AttributeError:
                    pass
                decoder.start_utt()
    else:
        break
decoder.end_utt()
print('An Error occured:', decoder.hyp().hypstr)
