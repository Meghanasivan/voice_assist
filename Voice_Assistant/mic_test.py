import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    r.energy_threshold = 400
    r.pause_threshold = 0.8
    print("🎙️ Speak something...")
    audio = r.listen(source, timeout=5)

    with open("mic_output.wav", "wb") as f:
        f.write(audio.get_wav_data())

    print("🔍 Trying to recognize...")
    try:
        text = r.recognize_google(audio)
        print("✅ You said:", text)
    except Exception as e:
        print("❌ Error:", e)
