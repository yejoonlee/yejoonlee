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

root_url = "https://www.instagram.com/robineleyartist/"
user_agent= "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36"


Driver = Driver(user_agent,root_url)
driver = Driver.start()

driver.find_elements_by_tag_name('a').click()

# driver.quit()
