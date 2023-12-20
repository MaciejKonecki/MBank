from datetime import time
from locators import logowanie_locators


class LodowaniePage:

    def __init__(self, driver):
        self.driver = driver
        self.login_input = logowanie_locators.LogowanieLocarotors.login_input
        self.password_input = logowanie_locators.LogowanieLocarotors.password_input
        self.przycisk_logowania = logowanie_locators.LogowanieLocarotors.przycisk_logowania

    def wprowadz_login(self, loginsent):
        login = self.driver.find_element(*self.login_input)
        login.send_keys(loginsent)
        time(1)

    def wprowadz_haslo(self, loginsent):
        password = self.driver.find_element(*self.password_input)
        password.click()
        password.send_keys(loginsent)
    def klikniecie_loguj(self):
        self.driver.find_element(*self.przycisk_logowania).click()