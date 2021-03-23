import pyttsx3

# inicialization
engine = pyttsx3.init()

# testing
engine.say("Olá, tudo bem?")
engine.say("Me diga como eu posso ajudar você?")
engine.say("Não, eu não quero te ajudar")

engine.runAndWait()
