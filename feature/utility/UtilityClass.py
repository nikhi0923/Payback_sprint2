from selenium import webdriver
from feature.utility.ConfigClass import ConfigClass


class UtilityClass:

    def __init__(self, driver):
        self.driver = driver

    def launch_browser(self):
        self.driver = webdriver.Chrome(ConfigClass.filePath)

    def launch_app(self):
        self.driver.maximize_window()
        self.driver.get(ConfigClass.url)

    def close_browser(self):
        self.driver.quit()

