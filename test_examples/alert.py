from time import sleep

from pytest import fixture
from selenium import webdriver
from selenium.webdriver.common.alert import Alert


@fixture
def driver():
    # cap = DesiredCapabilities.CHROME.copy()
    # cap['unexpectedAlertBehavior'] = "accept"
    opt = webdriver.ChromeOptions()
    opt.add_argument('--disable-popup-blocking')

    driver = webdriver.Chrome(executable_path='../drivers/chromedriver', options=opt)
    driver.maximize_window()
    yield driver
    driver.quit()


@fixture()
def driver_firefox():
    driver = webdriver.Firefox(executable_path='../drivers/geckodriver')
    driver.maximize_window()
    yield driver
    driver.quit()


def test_alert(driver):
    driver.get('http://beru.ru')
    driver.execute_script("alert('test_alert')")
    sleep(2)
    # depricated
    # alert = driver.switch_to_alert()

    alert = driver.switch_to.alert
    sleep(2)
    # Alert(driver).dismiss()
    sleep(2)
    print(alert.text)
    alert.accept()
    # sleep(4)


def test_prompt(driver_firefox):
    # не работает отображение в хром
    driver_firefox.get('http://beru.ru')
    driver_firefox.execute_script("prompt('Hello there!!!')")
    sleep(1)
    alert = driver_firefox.switch_to.alert
    alert.send_keys('Iam test alert')
    sleep(2)
    print(alert.text)
    # alert.accept()
    alert.dismiss()

def test_confirm(driver):
    driver.get('http://beru.ru')
    driver.execute_script("confirm('confirm_alert')")
    confirm = driver.switch_to.alert
    # alert.accept()
    # print(confirm.text)
    confirm.dismiss()

    # кликнуть на элемент, когда есть alert
    # el = driver.find_elements_by_css_selector("[data-zone-name='headerCatalog']")
    # el.click()


def test_simple(driver):
    driver.get('http://beru.ru')
    driver.execute_script("confirm('confirm_alert')")
    sleep(10)
    # confirm = driver.switch_to.alert
    # el = driver.find_element_by_css_selector("[data-zone-name='headerCatalog']")
    # el.click()
