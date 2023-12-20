import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
@pytest.fixture()
def setup(request):
    # można użyć niższego dostępu do webdrivera, mi jakoś nie idzie a już nie ma czasu tego poprawić :)
    # self.driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    beforFailed = request.session.testsfailed
    yield
    if request.session.testsfailed != beforFailed:
        allure.attach(driver.get_screenshot_as_png(), name = "Test failed", attachment_type=AttachmentType.PNG)
    driver.quit()