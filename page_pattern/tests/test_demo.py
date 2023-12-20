import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from page_pattern.pages.sprawdzenia_page import SprawdzenieAssercjiPage
from page_pattern.pages.strona_page import PrzejscieNaStroneLogowaniePage
from page_pattern.pages.logowanie_page import LodowaniePage
from page_pattern.pages.zalozenie_zadania_page import ZalozenieZadaniaPage

class TestyDemo:
    loginsent = 'administrator@testarena.pl'
    haslosent = 'sumXQQ72$L'
    tytulOpis = 'MK Zadaniev2'

    @pytest.fixture()
    def setup(self):
        #można użyć niższego dostępu do webdrivera, mi jakoś nie idzie a już nie ma czasu tego poprawić :)
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        time.sleep(1)
        yield
        self.driver.quit()

    def test_wejscie_na_strone(self, setup):
        self.driver.get("http://testarena.pl/demo")
        strona = PrzejscieNaStroneLogowaniePage(self.driver)
        logowanie = LodowaniePage(self.driver)
        strona.klik_demo()

        logowanie.wprowadz_login(self.loginsent)
        logowanie.wprowadz_haslo(self.haslosent)
        logowanie.klikniecie_loguj()

        time.sleep(5)

        zalozenieZadania = ZalozenieZadaniaPage(self.driver)
        zalozenieZadania.wejscie_na_zadania()
        zalozenieZadania.dodaj_zadanie()
        zalozenieZadania.uzupelnieni_pol(self.tytulOpis, "Oby się udało dostać pracę :)", "2021-07-29 23:59", "api", "test")
        zalozenieZadania.przypisz_do_mnie()
        zalozenieZadania.zapisz()

        zalozenieZadania.wejscie_na_zadania()
        print(self.tytulOpis)
        sprawdzenieAssert = SprawdzenieAssercjiPage(self.driver, self.tytulOpis)
        sprawdzenieAssert.czy_dodane_zadanie()

        strona.wyloguj()
        logowanie.wprowadz_login(self.loginsent)
        logowanie.wprowadz_haslo("sumXQQ72$Lopop")
        logowanie.klikniecie_loguj()
        sprawdzenieAssert.blad_logowania()
