from locators import sprawdzenie_locators
from locators.sprawdzenie_locators import Sprawdzenie_Locators


class SprawdzenieAssercjiPage:

    def __init__(self, driver, tytul_opis):
        self.tytul_opis = tytul_opis
        self.driver = driver
        self.zadanie_w_tabeli = Sprawdzenie_Locators.zadanie_w_tabeli(tytul_opis)
        self.error_komunikat = sprawdzenie_locators.Sprawdzenie_Locators.error_komunikat

    def get_tytuly_w_tabeli(self):
        tytul_pobrany = self.driver.find_element(*self.zadanie_w_tabeli)
        return [tytul_pobrany.text]

    def czy_dodane_zadanie(self):
        str = self.get_tytuly_w_tabeli()[0]
        assert self.tytul_opis == str, "Zadanie nie dodało się"

    def blad_logowania(self):
        self.driver.implicitly_wait(5)
        str = self.driver.find_element(*self.error_komunikat).text
        komunikt = "Adres e-mail i/lub hasło są niepoprawne."
        assert str == komunikt, "Udało się zalogować lub inny komunikat błęd"



