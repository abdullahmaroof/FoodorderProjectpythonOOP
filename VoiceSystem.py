import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

class call_voice:
    @staticmethod
    def wishme():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak('Good Morning!')
        elif hour>=12 and hour<18:
            speak('Good Afternoon!')
        else:
          speak('Good Evening!')
        speak('Welcome to our food order system')


class call_login(call_voice):
    @staticmethod
    def wishme():
        speak("Welcome to login sir. Please enter your username and password")

class voice_signup(call_voice):
    @staticmethod
    def wishme():
        speak("Welcome to signup new user. Please enter your information which is asked!!!")

class voice_loginadmin(call_voice):
    @staticmethod
    def wishme():
        speak("Welcome boss. Please enter your username and password for verification!!!")

class voice_system(call_voice):
    @staticmethod
    def wishme():
        speak("Sir, Click to order food for your meal")
        speak("or Click on about us to see our team")

class voice_menu(call_voice):
    @staticmethod
    def wishme():
        speak("Sir, tell us want you want to eat. We have all special meals")

class voice_pizza(call_voice):
    @staticmethod
    def wishme():
        speak("Sir, here you go with different pizza tastes. Place your order")

class voice_burger(call_voice):
    @staticmethod
    def wishme():
        speak("Sir, here you go with different burger tastes. Place your order")

class voice_biryani(call_voice):
    @staticmethod
    def wishme():
        speak("Sir, here you go with different biryani tastes. Place your order")

class voice_paratharoll(call_voice):
    @staticmethod
    def wishme():
        speak("Sir, here you go with different paratha roll tastes. Place your order")

class voice_admin(call_voice):
    @staticmethod
    def wishme():
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            speak('Boss,Good Morning!')
        elif hour >= 12 and hour < 18:
            speak('Boss,Good Afternoon!')
        else:
            speak('Boss,Good Evening!')
        speak("Boss, How are you!!!")
        speak("Boss, you can get reports of users, bills and menu")

class voice_aboutus(call_voice):
    @staticmethod
    def wishme():
        speak("Sir, you can see about our team!!!")

class voice_aboutabdullah(call_voice):
    @staticmethod
    def wishme():
        speak("Sir, This is our boss!!!")
        speak("Name: Abdullah Maroof")
        speak("Rollnumber: B A I M - F 19- 007")
        speak("section: 2 A")
        speak("Program: B S Artificial Intelligence")
        speak("Department: Software Engineering")
        speak("Student of Superior University, gold campus")

class voice_aboutZUBAIR(call_voice):
    @staticmethod
    def wishme():
        speak("Sir, This is our co boss!!!")
        speak("Name: Zubair Ali")
        speak("Rollnumber: B A I M - S 20- 009")
        speak("section: 2 A")
        speak("Program: B S Artificial Intelligence")
        speak("Department: Software Engineering")
        speak("Student of Superior University, gold campus")

class voice_bill(call_voice):
    @staticmethod
    def wishme():
        speak("Sir, this is your bill. Your order will serve you in 20 minutes!!!")

