import logging
import allure

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.__config_logger()

    def __config_logger(self):
        self.logger = logging.getLogger(type(self).__name__)
        file_handler = logging.FileHandler(f"/home/dissident/git/selenium_otus/logs/{self.browser.test_name}.log")
        file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
        self.logger.addHandler(file_handler)
        self.logger.setLevel(level=self.browser.log_level)

    def _wait_element(self, locator, timeout=3):
        self.logger.info(f'Wait element: {locator}')
        try:
            return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException as e:
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name="screenshot_image",
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(e.msg, "Cant find element by locator: {}".format(locator))

    def _element(self, locator):
        return self._wait_element(locator=locator)

    @allure.step
    def click(self, locator):
        self.logger.info(f'Click on: {locator}')
        element = self._element(locator)
        ActionChains(self.browser).pause(0.3).move_to_element(element).click().perform()

    @allure.step
    def accept_alert(self):
        self.logger.info('Accept alert')
        self.browser.switch_to.alert.accept()
