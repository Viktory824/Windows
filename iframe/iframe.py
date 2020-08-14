
from pytest import fixture
from selenium import webdriver
from time import sleep

# поднять локально http-server: python -m http.server 8080


@fixture
def driver():
    driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
    driver.maximize_window()
    yield driver
    driver.quit()


def test_iframe(driver):

    driver.get('http://localhost:8080')

    iframes = driver.find_elements_by_css_selector('iframe')

    driver.switch_to.frame('otus')
    courses = driver.find_element_by_xpath("//div[@class='header2__burger js-open-drawer']")
    courses.click()

    driver.switch_to.default_content()

    # driver.switch_to.frame(iframes[1])
    driver.switch_to.frame('avito')
    courses = driver.find_element_by_xpath("//a[text()='Авто']")
    courses.click()
    sleep(4)

    driver.switch_to.default_content()

    # driver.switch_to.frame(iframes[2])
    driver.switch_to.frame('selenium')
    close_win = driver.find_element_by_xpath("//button[@class='sendpulse-prompt-btn sendpulse-disallow-btn']")
    close_win.click()
    menu = driver.find_element_by_class_name('mobile-nav-trigger')
    menu.click()
    sleep(4)
