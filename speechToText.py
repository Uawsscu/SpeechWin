
import random
import pyttsx
engine = pyttsx.init()
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
voice = engine.getProperty('voice')
engine.setProperty('rate', 110) #Integer speech rate in words per minute.

# incoming and outgoing static response
qName = ["what is your name", "who are you", "whats your name"]
aName = ["i am called Jerry", "my name is Jerry"]
qGreeting = ["hi", "hi there", "hello", "How are you", "hello Jerry", "What's up"]
aGreeting = ["greetings", "hi", "hi there", "hello"]
qCommon1 = ["how are you", "how are you doing"]
aCommon1 = ["I am doing alright", "I am fine", "do ing great, and you?", "Great", "Pretty good", "Okay"]
qCommon2 = ["how was your day", "hows your day"]
aCommon2 = ["it was great", "just fine"]
qOnline = ["look for"]
interEro = ["No internet", "i can't go online", "connection is not available", "check internet connection", "check", "internet", "first", "no connection", "sorry internet is not available"]

#internet search function

while True:
    engine.say("Hello")
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
    engine.say(Ans)
    engine.runAndWait()
    pass
