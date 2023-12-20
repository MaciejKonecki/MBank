from locators import strona_locators


class PrzejscieNaStroneLogowaniePage:
    def __init__(self, driver):
        self.driver = driver
        self.przycisk_demo = strona_locators.StronaLocators.przycisk_demo
        self.wyloguj_button = strona_locators.StronaLocators.wyloguj_button

    def klik_demo(self):
        current_window = self.driver.current_window_handle
        all_windows = self.driver.window_handles

        self.driver.find_element(*self.przycisk_demo).click()

        new_window = set(self.driver.window_handles) - set(all_windows)
        new_window_id = new_window.pop()
        self.driver.switch_to.window(new_window_id)

    def wyloguj(self):
        self.driver.find_element(*self.wyloguj_button).click()
