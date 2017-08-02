import re
import sqlite3
from collections import Counter
from string import punctuation
from math import sqrt
import random
import socket
import wikipedia

import pyttsx
engine = pyttsx.init()
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
voice = engine.getProperty('voice')
engine.setProperty('rate', 110) #Integer speech rate in words per minute.

# initialize the connection to the database
connection = sqlite3.connect('brain1.sqlite')
cursor = connection.cursor()

# create the tables needed by the program
create_table_request_list = [
    'CREATE TABLE words(word TEXT UNIQUE)','CREATE TABLE sentences(sentence TEXT UNIQUE, used INT NOT NULL DEFAULT 0)',    'CREATE TABLE associations (word_id INT NOT NULL, sentence_id INT NOT NULL, weight REAL NOT NULL)',]
for create_table_request in create_table_request_list:
    try:
        cursor.execute(create_table_request)
    except:
        pass

def get_id(entityName, text):
    """Retrieve an entity's unique ID from the database, given its associated text. If the row is not already present, it is inserted. The entity can either be a sentence or a word."""
    tableName = entityName+'s'
    columnName = entityName
    cursor.execute('SELECT rowid FROM '+tableName+' WHERE '+columnName+' = ?', (text,))
    row = cursor.fetchone()
    if row:
        return row[0]
    else:
        cursor.execute('INSERT INTO '+tableName+' ('+columnName+') VALUES (?)', (text,))
        return cursor.lastrowid


def get_words(text):
    """"Retrieve the words present in a given string of text. The return value is a list of tuples where the first member is a lowercase word, and the second member the number of time it is present in the text."""
    wordsRegexpString = '(?:\w+|['+re.escape(punctuation)+']+)'
    wordsRegexp = re.compile(wordsRegexpString)
    wordsList = wordsRegexp.findall(text.lower())
    return Counter(wordsList).items()


# incoming and outgoing static response
qName = ["what is your name", "who are you", "whats your name"]
aName = ["i am called Jerry", "my name is Jerry"]
qGreeting = ["hi", "hi there", "hello", "How are you", "hello Jerry", "What's up"]
aGreeting = ["greetings", "hi", "hi there", "hello"] #random picking up from here
qCommon1 = ["how are you", "how are you doing"]
aCommon1 = ["I am doing alright", "I am fine", "do ing great, and you?", "Great", "Pretty good", "Okay"]
qCommon2 = ["how was your day", "hows your day"]
aCommon2 = ["it was great", "just fine"]
qOnline = ["look for"]
interEro = ["No internet", "i can't go online", "connection is not available", "check internet connection", "check", "internet", "first", "no connection", "sorry internet is not available"]

#internet search function
B = random.choice(aGreeting)
while True:
    def online():
        interp = "google.com"
        try:
            host = socket.gethostbyname(interp)
            socket.create_connection((host, 80), 2)
            print("I am online now ask me anything\n")
            i = input('> ').strip()
            query = i.lower()
            print("Search...")
            ans = wikipedia.summary(query)
            print("> "+ans)
            row = ans
            r = row[1]
            cursor.execute('UPDATE sentences SET used=used+1 WHERE rowid=?', (row[0],))
            print('online> '+r)
        except Exception :
            print("> "+random.choice(interEro))
            return

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
    elif H == "wiki":
        online()
    else:
        print(":~# ????")
        continue

    print(":~# " + Ans)
    engine.say(Ans)
    engine.runAndWait()
