from selenium import webdriver
from selenium.webdriver.chrome.options import Options

DRIVER_DIR = "/Users/nezmi/Downloads/chromedriver"

class Driver:
    def __init__(self,user_agent,root_url):
        self.opt = Options()
        self.opt.add_argument("user-agent= %s" %user_agent)
        self.root_url = root_url

    def start(self):
        driver = webdriver.Chrome(DRIVER_DIR, chrome_options=self.opt)
        driver.implicitly_wait(5)

        driver.get(self.root_url)

        return driver