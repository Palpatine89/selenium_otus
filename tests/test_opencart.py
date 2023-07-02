from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_main_page(browser):
    browser.get(browser.url)
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#cart")))
    browser.find_element(By.CSS_SELECTOR, "#logo")
    browser.find_element(By.CSS_SELECTOR, "[name=search]")
    browser.find_element(By.CSS_SELECTOR, "[title~=MacBook]")
    browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[3]/button[1]')


def test_tablet_page(browser):
    browser.get(browser.url + "/tablet")
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#grid-view")))
    browser.find_element(By.CSS_SELECTOR, "#list-view")
    browser.find_element(By.CSS_SELECTOR, "#input-limit")
    browser.find_element(By.CSS_SELECTOR, "#input-sort")
    browser.find_element(By.XPATH, '//*[@id="content"]/div[3]/div[2]')


def test_product_card_page(browser):
    browser.get(browser.url + "/tablet/samsung-galaxy-tab-10-1")
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#button-cart")))
    browser.find_element(By.CSS_SELECTOR, "a[href^='#tab-description']")
    browser.find_element(By.CSS_SELECTOR, "a[href^='#tab-review']")
    browser.find_element(By.CSS_SELECTOR, "[name=quantity]")
    browser.find_element(By.CSS_SELECTOR, "[data-original-title~=Compare]")


def test_admin_page(browser):
    browser.get(browser.url + "/admin")
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[name=username]")))
    browser.find_element(By.CSS_SELECTOR, "#input-password")
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]")
    browser.find_element(By.CSS_SELECTOR, "span > a[href$='route=common/forgotten']")
    browser.find_element(By.CSS_SELECTOR, "[title~=OpenCart]")


def test_register_page(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[name=firstname]")))
    browser.find_element(By.CSS_SELECTOR, "#input-password")
    browser.find_element(By.CSS_SELECTOR, "input[type=checkbox]")
    browser.find_element(By.CSS_SELECTOR, "input[type=submit]")
    browser.find_element(By.CSS_SELECTOR, "input[type=radio]")
