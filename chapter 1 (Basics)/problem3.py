# importing the pyttsx library 
import pyttsx3 

# initialisation 
engine = pyttsx3.init() 

# testing 
engine.say("My first code on text-to-speech") 

# engine.say("Thank you, Sagar Raj") 
# engine.say("Sagar Raj is a GOD") 

for i in range(4):
  engine.say("jai bhavani")
engine.runAndWait() 
