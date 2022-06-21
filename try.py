import speech_recognition as sr  
import webbrowser

r = sr.Recognizer()  
 
mic = sr.Microphone(device_index = 1)  
 
with mic as source:  
    r.adjust_for_ambient_noise(source, duration = 1)  
    print("Say something")  
    audio = r.listen(source, timeout = 7)  
    print("Time's up, Thanks!!")  
 
try:  

#end
print("opening browser...........")
webbrowser.register('chrome',
None,
webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
webbrowser.get('chrome').open_new(search)
