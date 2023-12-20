# # import ChromeDriverManager
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.remote.webdriver import WebDriver
# from selenium.webdriver.support.wait import WebDriverWait
#
# loginsent = 'administrator@testarena.pl'
# haslosent = 'sumXQQ72$L'
#
# web_driver: WebDriver = webdriver.Chrome()
# web_driver.get("http://testarena.pl/demo")
# web_driver.maximize_window()
# time.sleep(1)
# current_window = web_driver.current_window_handle
# all_windows = web_driver.window_handles
#
# element = web_driver.find_element(By.ID, "example")
# element2 = web_driver.find_element(By.XPATH, "//div[@class='description']/p[2]/a[1]")
# element2.click()
# time.sleep(1)
#
# # Pobierz identyfikator nowo otwartej karty
# new_window = set(web_driver.window_handles) - set(all_windows)
# new_window_id = new_window.pop()
#
# # Przełącz się na nową kartę
# web_driver.switch_to.window(new_window_id)
#
#
# login = web_driver.find_element(By.XPATH, "//input[@id='email']")
# login.send_keys(loginsent)
# time.sleep(1)
# # poprawic
# password = web_driver.find_element(By.XPATH, "//input[@id='password']")
# password.click()
# password.send_keys(haslosent)
# web_driver.find_element(By.XPATH, "//input[@id='login']").click()
#
# # Tworzenie zadania
# web_driver.find_element(By.XPATH, "//a[@class='activeMenu']").click()
# web_driver.find_element(By.XPATH, "//a[@class='button_link']").click()
# tytul = web_driver.find_element(By.XPATH, "//input[@id='title']").click()
# tytul.send_keys("MK Zadanie")
# opis = web_driver.find_element(By.XPATH, "//textarea[@id='description']").click()
# opis.send_keys("Oby się udało dostać pracę :)")
# web_driver.find_element(By.XPATH, "//a[@id='j_assignToMe']").click()
#
# web_driver.find_element(By.XPATH, "//input[@id='save']").click()
#
#
# time.sleep(5)