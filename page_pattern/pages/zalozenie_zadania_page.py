import time

import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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
        wait5 = WebDriverWait(self.driver, 5, 0.5)

    @allure.step("Wejście na zadanie")
    def wejscie_na_zadania(self):
        self.driver.find_element(*self.zadania_zakladka_button).click()

    @allure.step("Dodaj zadanie")
    def dodaj_zadanie(self):
        self.wait5.until(expected_conditions.visibility_of_element_located(*self.dodaj_zadanie_button))
        self.driver.find_element(*self.dodaj_zadanie_button).click()
        time.sleep(1)

    @allure.step("Uzupełnianie pól")
    def uzupelnieni_pol(self, opisTytul, opisOpis, terminOpis, srodowiskoOpis, wersjeOpis):
        self.wait5.until(expected_conditions.visibility_of_element_located(*self.tytul_input))
        tytul = self.driver.find_element(*self.tytul_input)
        tytul.send_keys(opisTytul)
        opis = self.driver.find_element(*self.opis_input)
        opis.send_keys(opisOpis)
        srodowisko = self.driver.find_element(*self.srodowiska_input)
        srodowisko.send_keys(srodowiskoOpis)
        time.sleep(1) # zostawiłem gdyż nie ma o co zachaczyć waita, a implicitly_wait nie jest potrzebna do całego kodu
        srodowisko.send_keys(Keys.ENTER)
        time.sleep(1)# zostawiłem gdyż nie ma o co zachaczyć waita, a implicitly_wait nie jest potrzebna do całego kodu
        wersje = self.driver.find_element(*self.wersje_input)
        wersje.send_keys(wersjeOpis)
        time.sleep(1)# zostawiłem gdyż nie ma o co zachaczyć waita, a implicitly_wait nie jest potrzebna do całego kodu
        wersje.send_keys(Keys.ENTER)
        time.sleep(1)# zostawiłem gdyż nie ma o co zachaczyć waita, a implicitly_wait nie jest potrzebna do całego kodu
        termin = self.driver.find_element(*self.termin_input)
        termin.send_keys(terminOpis)
        termin.send_keys(Keys.ENTER)

    @allure.step("Przyisz do mnie")
    def przypisz_do_mnie(self):
        self.driver.find_element(*self.przypisz_do_nie_button).click()

    @allure.step("Zapisz")
    def zapisz(self):
        self.driver.find_element(*self.zapisz_button).click()