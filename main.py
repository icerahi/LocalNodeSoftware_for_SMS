from selenium.webdriver import Firefox,Chrome
from selenium.webdriver.chrome.options import Options
options = Options()

options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
options.add_argument("--use-fake-ui-for-media-stream")
options.add_argument("--start-fullscreen")
#options.add_argument("--kiosk")
browser = Chrome(executable_path="./chromedriver",options=options)
browser.get(" http://127.0.0.1:8000/")

browser.fullscreen_window()

