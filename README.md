#Jarvis Voice Assistant



Jarvis is a simple voice assistant built in Python that can perform tasks such as playing songs on YouTube, telling the time and date, answering basic questions, and searching Wikipedia. It uses speech recognition to understand user commands and text-to-speech to respond.

Features
Voice Command Recognition: Listen to commands using your microphone.

Text-to-Speech: Responds verbally to commands using pyttsx3.

Play Songs: Play songs directly on YouTube via pywhatkit.

Tell Time and Date: Gives the current time and date.

Basic Conversation: Can answer questions like "How are you?" and "What is your name?".

Wikipedia Search: Fetches and displays summaries from Wikipedia.

Technologies Used
Python 3

speech_recognition – for converting speech to text

pyttsx3 – for text-to-speech

pywhatkit – to play songs on YouTube

datetime – for getting current time and date

wikipedia & wikipedia-api – for searching and summarizing Wikipedia articles

pyaudio – for accessing the microphone

Installation
Clone this repository:

bash
Copy code
git clone https://github.com/yourusername/Jarvis-Voice-Assistant.git
Navigate to the project folder:

bash
Copy code
cd Jarvis-Voice-Assistant
Install required packages:

bash
Copy code
pip install -r requirements.txt
If you don’t have a requirements.txt, install manually:

bash
Copy code
pip install SpeechRecognition pyttsx3 pywhatkit pyaudio wikipedia wikipedia-api
Usage
Run the Python script:

bash
Copy code
python jarvis.py
You can type your command or speak (if the speech recognition is enabled). Example commands:

"play [song name]" → Plays the song on YouTube

"what is the time" → Shows and speaks the current time

"what is the date" → Shows and speaks the current date

"how are you" → Jarvis responds

"wikipedia [topic]" → Fetches and displays a summary from Wikipedia

Note: Make sure your microphone is connected and working for voice commands.

How It Works
Input: Jarvis listens to your command either through text input or voice input.

Processing: It identifies keywords like play, time, date, or wikipedia.

Response: Performs the requested action (plays a song, gives time/date, answers questions, or fetches Wikipedia summary).

Output: Speaks the response and prints relevant information to the console.

Future Improvements
Enable continuous voice listening without needing to type commands.

Add more conversational AI responses.

Integrate with other APIs like weather, news, or smart home devices.

Error handling for unavailable YouTube videos or Wikipedia pages.

License
This project is open-source and free to use.
