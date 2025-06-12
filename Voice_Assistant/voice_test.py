
import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
print("Available voices:")
for index, voice in enumerate(voices):
    print(f"{index}: {voice.name} - {voice.id}")

engine.setProperty('voice', voices[0].id)  # Try using first available voice
engine.setProperty('rate', 150)  # Speaking speed

print("🔊 Trying to speak...")
engine.say("Hello Meghna, testing text to speech.")
engine.runAndWait()
print("✅ Done speaking.")
