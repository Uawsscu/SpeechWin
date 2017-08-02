import random
from espeak import espeak
espeak.set_parameter(espeak.Parameter.Pitch, 60)
espeak.set_parameter(espeak.Parameter.Rate, 110)
espeak.set_parameter(espeak.Parameter.Range, 600)

espeak.synth("Hey Guys")
# incoming and outgoing static response
qName = ["what is your name", "who are you", "whats your name"]
aName = ["i am called Jerry", "my name is Jerry"]
qGreeting = ["hi", "hi there", "hello", "How are you", "hello Jerry", "what's up"]
aGreeting = ["greetings", "hi", "hi there", "hello"]
qCommon1 = ["how are you", "how are you doing"]
aCommon1 = ["I am doing alright", "I am fine", "do ing great, and you?", "great", "pretty good", "okay"]
qCommon2 = ["how was your day", "hows your day"]
aCommon2 = ["it was great", "just fine"]
qOnline = ["look for"]
interEro = ["no internet", "i can't go online", "connection is not available", "check internet connection", "check", "internet", "first", "no connection", "sorry internet is not available"]

#internet search function

while True:
    # ask for user input; if blank line, exit the loop
    H = raw_input(':~# ')

    if H == "":
        print(":~# sorry can't get it")
        exit()
# fire up internet function    #
    if H in qName:
        Ans=random.choice(aName)
    elif H in qGreeting:
        Ans =random.choice(aGreeting)
    elif H in qCommon1:
        Ans =random.choice(aCommon1)
    elif H in qCommon2:
        Ans = random.choice(aCommon2)
    else:
        print(":~# ????")
        continue
    print(":~# " + Ans)

    espeak.synth(Ans)
    pass
