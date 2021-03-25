import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import random
import wolframalpha

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")
            speak("opening youtube")

        elif 'open google' in query:
            webbrowser.open("https://google.com")
            speak("opening google")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")
            speak("opening stackoverflow") 

        elif 'open github' in query:
            webbrowser.open("https://www.github.com")
            speak("opening github")
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")
            speak("opening facebook")      
        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")
            speak("opening instagram")  
            
        elif 'open yahoo' in query:
            webbrowser.open("https://www.yahoo.com")
            speak("opening yahoo")
            
        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com")
            speak("opening google mail") 
        elif 'open snapdeal' in query:
            webbrowser.open("https://www.snapdeal.com") 
            speak("opening snapdeal")  
             
        elif 'open amazon' in query or 'shop online' in query:
            webbrowser.open("https://www.amazon.com")
            speak("opening amazon")
        elif 'open flipkart' in query:
            webbrowser.open("https://www.flipkart.com")
            speak("opening flipkart")   
        elif 'open ebay' in query:
            webbrowser.open("https://www.ebay.com")
            speak("opening ebay") 
        elif 'music from pc' in query or "music" in query:
            speak("ok i am playing music")
            music_dir = 'c://mu'
            musics = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,musics[0]))
        elif 'video from pc' in query or "video" in query:
            speak("ok i am playing videos")
            video_dir = 'c://videos'
            videos = os.listdir(video_dir)
            os.startfile(os.path.join(video_dir,videos[0])) 
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'the date' in query:
            strDate = datetime.datetime.now().strftime("%A, %B %d, %Y")    
            speak(f"Sir,the day is yours, and the Date is {strDate}")
        elif 'the day' in query:
            strDay = datetime.datetime.now().strftime("%A")    
            speak(f"Sir,the day is yours, and it is {strDay}")
        elif 'calculate' in query:
            try:
                app_id = "8JR6EV-3J8599QHTH"
                client = wolframalpha.Client(app_id)
                indx = query.lower().split().index('calculate')
                query =query.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                print("the answer is " + answer)
                speak("the answer is " + answer)
            except Exception as e:
                print(e)
                speak("please ask numbers to calculate and with accurate pronunciation")



        elif 'open code' in query:
            codePath = "C:\\Users\\admin\\AppData\\Local\\Programs\\Microsoft VS Code"
            os.startfile(codePath)

        elif 'email to saurabh' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "saurabhv.pandey5@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email") 
        elif 'good bye' in query:
            speak("good bye")
            exit()
        elif "shutdown" in query:
            speak("shutting down")
            os.system('shutdown -s') 
        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!How are you', 'I am fine!,how are you?', 'Nice!what about you?', 'I am nice and full of energy, how you are?','i am okay! How are you?']
            ans_q = random.choice(stMsgs)
            speak(ans_q)  
            ans_take_from_user_how_are_you = takeCommand()
            if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okey' in ans_take_from_user_how_are_you:
                speak('okey..')  
            elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
                speak('oh sorry..')  
        elif 'make you' in query or 'created you' in query or 'develop you' in query or 'made you' in query:
            ans_m = " For your information Saurabh Created me ! I give Lot of Thannks to Him "
            print(ans_m)
            speak(ans_m)
        elif 'about Saurabh' in query or 'who is Saurabh' in query:
            ans = " His full name is Saurabh Pandey and he made me as a project for his College, he currently  is a student and also a teacher"
            print(ans)
            speak(ans)
        elif "who are you" in query or "about you" in query or "your details" in query:
            about = "I am Jarvis an A I based computer program but i can help you lot like a your close friend ! i promise you ! Simple try me to give simple command ! like playing music or video from your directory i also play video and song from web or online ! i can also entain you i so think you Understand me ! ok Lets Start "
            print(about)
            speak(about)
        elif "hello" in query or "hello Jarvis" in query:
            hel = "Hello Saurabh Sir ! How May i Help you.."
            print(hel)
            speak(hel)
        elif "your name" in query or "sweet name" in query:
            na_me = "Thanks for Asking my name my self ! Jarvis"  
            print(na_me)
            speak(na_me)
        elif "you feeling" in query:
            print("feeling Very good after meeting with you")
            speak("feeling Very good after meeting with you") 
        elif query == 'none':
            continue 
        elif 'exit' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'quit' in query :
            ex_exit = 'I feeling very sweet after meeting with you but you are going! i am very sad'
            speak(ex_exit)
            exit()    
        else:
            temp = query.replace(' ','+')
            g_url="https://www.google.com/search?q="    
            res_g = 'sorry! i cant understand but i search from internet to give your answer ! okay'
            print(res_g)
            speak(res_g)
            webbrowser.open(g_url+temp)
        