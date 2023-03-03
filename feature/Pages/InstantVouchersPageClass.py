import time


from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class InstantVouchersPageClass:

    def __init__(self, driver):
        self.driver = driver

        # Element Locators Values
        self.searchBarElement = "//input[@type='search'][1]"
        self.searchLogoElement = "//img[@src='/payback/static/images/search.png'][1]"
        self.searchdropdownElement = "(//*[text()='KFC'])[1]"
        self.chatassistanticon = "//*[@class='chat-icon']"
        self.voucherbutton = "(//*[@class='question-option cus-color'])[1]"

    
    def Search_Bar_TextBox(self):
       searchBarTextBox = self.driver.find_element(By.XPATH, self.searchBarElement)
       searchBarTextBox.click()
       searchBarTextBox.send_keys("KFC")
       time.sleep(3)
       searchBarTextBox.clear()
       time.sleep(2)

       print("searchTextbox is  working")

    def search_icon(self):
        searchbartext = self.driver.find_element(By.XPATH, self.searchBarElement)
        searchbartext.click()
        searchbartext.send_keys("KFC")
        time.sleep(3)
        searchIcon = self.driver.find_element(By.XPATH,self.searchLogoElement)
        searchIcon.click()
        time.sleep(3)

    def invalid_text(self):
        invalidtext = self.driver.find_element(By.XPATH, self.searchBarElement)
        invalidtext.click()
        invalidtext.send_keys("xyz")
        time.sleep(2)
        searchIcon = self.driver.find_element(By.XPATH, self.searchLogoElement)
        searchIcon.click()
        time.sleep(2)

    def select_text(self):
        selecttext = self.driver.find_element(By.XPATH, self.searchdropdownElement)
        action = ActionChains(self.driver)
        action.move_to_element(selecttext)
        action.perform()
        selecttext.click()
        time.sleep(3)

    def chat_icon(self):
        time.sleep(4)
        chaticon = self.driver.find_element(By.XPATH, self.chatassistanticon)
        chaticon.click()
        time.sleep(3)


    def click_button(self):
        time.sleep(3)
        voucherbutton = self.driver.find_element(By.XPATH,self.voucherbutton)
        voucherbutton.click()
        time.sleep(5)


















