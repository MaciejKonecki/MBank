from selenium.webdriver.common.by import By


class StronaLocators:
    przycisk_demo = (By.XPATH, "//div[@class='description']/p[2]/a[1]")
    wyloguj_button = (By.XPATH, "//a[@href='http://demo.testarena.pl/wyloguj']")
