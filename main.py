import threading

from selenium.webdriver import Firefox,Chrome
from selenium.webdriver.chrome.options import Options
import os
def server():
    os.system('python manage.py runserver 0.0.0.0:8000')

def screen():
    options = Options()
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("--use-fake-ui-for-media-stream")
    options.add_argument("--start-fullscreen")
    #options.add_argument("--kiosk")
    browser = Chrome(executable_path="./chromedriver",options=options)
    browser.get(" http://127.0.0.1:8000/")
    browser.fullscreen_window()

if __name__ == "__main__":
    t1=threading.Thread(target=server)
    t2=threading.Thread(target=screen)
    t1.start()
    t2.start()
