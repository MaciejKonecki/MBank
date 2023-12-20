from selenium.webdriver.common.by import By


class Sprawdzenie_Locators:

    error_komunikat = (By.XPATH, "//div[@class='login_form_error']")

    @staticmethod
    def zadanie_w_tabeli(tytulZadania):
        return (By.XPATH, f"//a[contains(text(), '{tytulZadania}')]")
