from selenium.webdriver.common.by import By


class ZalozenieZadaniaLocators:
    zadania_zakladka_button = (By.XPATH, "//a[contains(text(), 'Zadania')]")
    dodaj_zadanie_button = (By.XPATH, "//a[@class='button_link']")
    tytul_input = (By.XPATH, "//input[@id='title']")
    opis_input = (By.XPATH, "//textarea[@id='description']")
    przypisz_do_nie_button = (By.XPATH, "//a[@id='j_assignToMe']")
    zapisz_button = (By.XPATH, "//input[@id='save']")
    wersje_input = (By.XPATH, "//input[@id='token-input-versions']")
    srodowiska_input = (By.XPATH, "//input[@id='token-input-environments']")
    termin_input = (By.XPATH, "//input[@id='dueDate']")
