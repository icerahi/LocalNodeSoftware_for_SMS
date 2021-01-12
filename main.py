from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
options = Options()
options.add_argument("--start-fullscreen")
options.add_argument("--kiosk")
browser = Firefox(executable_path="./geckodriver",options=options)
browser.get("http://localhost:8000")

browser.fullscreen_window()
