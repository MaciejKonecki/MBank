from selenium.webdriver.common.by import By


class LogowanieLocarotors:
    login_input = (By.XPATH, "//input[@id='email']")
    password_input = (By.XPATH, "//input[@id='password']")
    przycisk_logowania = (By.XPATH, "//input[@id='login']")