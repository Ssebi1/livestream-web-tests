import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


class Driver:
    def __init__(self):
        self.driver = None

    def create_chrome_driver(self, headless=True, driver_path=None):

        try:
            chrome_options = ChromeOptions()
            if headless:
                chrome_options.add_argument("--headless")
            chrome_options.add_argument("--window-size=1920,1080")
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--disable-blink-features")
            chrome_options.add_argument("--disable-blink-features=AutomationControlled")
            if driver_path is not None:
                self.driver = webdriver.Chrome(options=chrome_options, executable_path=driver_path)
            else:
                self.driver = webdriver.Chrome(options=chrome_options)
        except Exception as e:
            raise Exception('Something went wrong. Cannot initialize chrome driver, make sure that it is installed.')