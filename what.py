import pyttsx3

def say (text) :
    engine.say(text)
    print(text)
    engine.runAndWait()

engine = pyttsx3.init()
say("Name: Jelaine Alexa Maigue")
say("Age: 18 years old")
say("Address: 30-A Dahlia St. Brgy. Old Capitol Site, Diliman, Quezon City")