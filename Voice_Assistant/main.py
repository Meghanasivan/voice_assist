import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# 🔊 Voice configuration
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Change to voices[1].id if needed
engine.setProperty('rate', 150)

# Function to speak text aloud
def speak(text):
    print(f"🗣️ Assistant says: {text}")
    engine.say(text)
    engine.runAndWait()

# Function to listen and recognize speech
def get_command():
    with sr.Microphone() as source:
        recognizer.energy_threshold = 600      # Adjust based on your environment
        recognizer.pause_threshold = 0.8        # Waits for 0.8s of silence
        print("🎙️ Listening... (say something)")

        try:
            audio = recognizer.listen(source, timeout=5)
        except sr.WaitTimeoutError:
            print("⏱️ No speech detected.")
            speak("I didn't hear anything. Try again.")
            return ""

        # (Optional) Save audio to file for testing/debugging
        with open("last_input.wav", "wb") as f:
            f.write(audio.get_wav_data())

        try:
            print("🔍 Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"✅ You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("❌ Could not understand audio.")
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            print("❌ Could not connect to the recognition service.")
            speak("Network error.")
            return ""

# Main assistant logic
def run_assistant():
    while True:
        command = get_command()

        if "hello" in command:
            speak("Hello Meghna, how can I help you?")
        
        elif "time" in command:
            now = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {now}")
        
        elif "search" in command:
            speak("What should I search?")
            query = get_command()
            if query:
                webbrowser.open(f"https://www.google.com/search?q={query}")
                speak(f"Searching Google for {query}")
        
        elif "stop" in command or "exit" in command:
            speak("Goodbye Meghna!")
            break

# Start the assistant
if __name__ == "__main__":
    print("✅ Assistant is ready. Speak now!")
    speak("Voice Assistant is now active.")
    run_assistant()

