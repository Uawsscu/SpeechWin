
from os import environ, path
import pyaudio

from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *

from sys import stdout #Grammar
#https://stackoverflow.com/questions/38808776/python-pocketsphinx-recognition-from-the-microphone


MODELDIR = "/home/uawsscu/speech_recognition/pocketsphinx/model"
DATADIR = "/home/uawsscu/speech_recognition/pocketsphinx/test/data"

config = Decoder.default_config()
config.set_string('-hmm', path.join(MODELDIR, 'en-us/en-us'))
config.set_string('-lm', path.join(MODELDIR, 'en-us/en-us.lm.bin'))
config.set_string('-dict', path.join(MODELDIR, 'en-us/cmudict-en-us.dict'))
decoder = Decoder(config)

# Switch to JSGF grammar
jsgf = Jsgf(path.join(DATADIR, 'goforward.gram'))
rule = jsgf.get_rule('goforward.move2')
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
        if decoder.get_in_speech() != in_speech_bf:
            in_speech_bf = decoder.get_in_speech()
            if not in_speech_bf:
                decoder.end_utt()
                hypothesis = decoder.hyp()
                print 'Result: ', hypothesis.hypstr
                decoder.start_utt()
    else:
        break
decoder.end_utt()
