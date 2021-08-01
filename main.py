import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak the message:")
    audio= r.lsiten(source)
    query = r.recognize_google(audio)
    print(query)