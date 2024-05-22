import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import pyaudio
import wikipediaapi
import wikipedia as wiki

 

listener = aa.Recognizer()

machine = pyttsx3.init()

def talk(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def input_instruction():
    global instruction
    try:
     with aa.Microphone() as origin:
         print("Listening")
         speech = listener.listen(origin)
         instruction = listener.recognize_google(speech)
         instruction=instruction.lower()
         if "jarvis" in instruction:
             instruction=instruction.replace("jarvis","")
             print(instruction)
             print("lisinting....")
             
    except aa.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except aa.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except aa.WaitTimeoutError:
        print("Timeout listening to microphone.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return instruction

def play_Jarvis():
    instruction = input("How can I help you? ")  # Get user input
    #instruction = input_instruction()
    print(instruction)
    if instruction is not None and "play" in instruction:
        song = instruction.replace("play", "")
        talk("Playing " + song)
        pywhatkit.playonyt(song)  # Assuming you want to play the song from YouTube

    elif instruction is not None and "time" in instruction:
        current_time = datetime.datetime.now().strftime('%H:%M:%S')  # Get current time
        talk("Current time is " + current_time)
        val1=(current_time)
        print(val1)

    elif instruction is not None and "date" in instruction:
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')  # Get current date
        talk("Today's date is " + current_date)

    elif instruction is not None and "How are you" in instruction:
        talk("I am fine")
        val=('I am fine')
        print(val)

    elif instruction is not None and "what is your name" in instruction:
        talk("I am Jarvis")
    elif instruction is not None and "wikipedia" in instruction:
        result=wiki.search(input("what you want to search"))
        for search in result:
            print(search)
            print(wiki.page(search).summary)
    
    
     
        

            
        
            
        
        
            
    else:
        talk("Please repeat")  # In case none of the conditions match

play_Jarvis()



        
        
    
        
    
