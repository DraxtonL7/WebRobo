import webbrowser
import time
import keyboard
from pynput.keyboard import Key, Controller

while True:
    search_term = "https://imgur.com/gallery/oQKI2j9"
    url = "https://www.google.com.tr/search?q={}".format(search_term)
    webbrowser.open(url)
    time.sleep(2)
    Keyboard = Controller()

    def tab():
        Keyboard.press(Key.tab)
        Keyboard.release(Key.tab)
        
    for i in range(0,19):
        tab()
    Keyboard.press(Key.enter)
    time.sleep(3)

    if keyboard.is_pressed('q'):
        print("Stopping")
        break
print("The End")
