import time

from selenium.webdriver.common.keys import Keys
from locators import zalozenie_zadania_locators

class ZalozenieZadaniaPage:

    def __init__(self, driver):
        self.driver = driver
        self.tytul_input = zalozenie_zadania_locators.ZalozenieZadaniaLocators.tytul_input
        self.opis_input = zalozenie_zadania_locators.ZalozenieZadaniaLocators.opis_input
        self.srodowiska_input = zalozenie_zadania_locators.ZalozenieZadaniaLocators.srodowiska_input
        self.wersje_input = zalozenie_zadania_locators.ZalozenieZadaniaLocators.wersje_input
        self.termin_input = zalozenie_zadania_locators.ZalozenieZadaniaLocators.termin_input
        self.przypisz_do_nie_button = zalozenie_zadania_locators.ZalozenieZadaniaLocators.przypisz_do_nie_button
        self.zapisz_button = zalozenie_zadania_locators.ZalozenieZadaniaLocators.zapisz_button
        self.dodaj_zadanie_button = zalozenie_zadania_locators.ZalozenieZadaniaLocators.dodaj_zadanie_button
        self.zadania_zakladka_button = zalozenie_zadania_locators.ZalozenieZadaniaLocators.zadania_zakladka_button
    def wejscie_na_zadania(self):
        self.driver.find_element(*self.zadania_zakladka_button).click()
        time.sleep(1)

    def dodaj_zadanie(self):
        self.driver.find_element(*self.dodaj_zadanie_button).click()
        time.sleep(1)

    def uzupelnieni_pol(self, opisTytul, opisOpis, terminOpis, srodowiskoOpis, wersjeOpis):
        tytul = self.driver.find_element(*self.tytul_input)
        tytul.send_keys(opisTytul)
        opis = self.driver.find_element(*self.opis_input)
        opis.send_keys(opisOpis)
        srodowisko = self.driver.find_element(*self.srodowiska_input)
        srodowisko.send_keys(srodowiskoOpis)
        time.sleep(1)
        srodowisko.send_keys(Keys.ENTER)
        time.sleep(1)
        wersje = self.driver.find_element(*self.wersje_input)
        wersje.send_keys(wersjeOpis)
        time.sleep(1)
        wersje.send_keys(Keys.ENTER)
        time.sleep(1)
        termin = self.driver.find_element(*self.termin_input)
        termin.send_keys(terminOpis)
        termin.send_keys(Keys.ENTER)

    def przypisz_do_mnie(self):
        self.driver.find_element(*self.przypisz_do_nie_button).click()

    def zapisz(self):
        self.driver.find_element(*self.zapisz_button).click()