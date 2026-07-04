from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class KeywordLibrary:

    def __init__(self):
        self.driver = None
        self.wait = None

    def OpenBrowser(self, url):
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(url)

    def InputText(self, fieldId, value):
        element = self.wait.until(
            EC.visibility_of_element_located((By.ID, fieldId))
        )
        element.clear()
        element.send_keys(value)

    def ClickElement(self, selector):
        element = self.wait.until(
            EC.element_to_be_clickable((By.ID, selector))
        )
        element.click()

    def VerifyTextPresent(self, text):
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.TAG_NAME, "body"),
                text
            )
        )

    def AddToCartByIndex(self, index):
        buttons = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "button.btn_inventory")
            )
        )

        if index < 0 or index >= len(buttons):
            raise IndexError(
                f"Product index {index} does not exist."
            )

        buttons[index].click()

    def CloseBrowser(self):
        if self.driver:
            self.driver.quit()
