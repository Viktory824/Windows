from os import path
from time import sleep

from pytest import fixture
from selenium import webdriver


@fixture
def driver():
    driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
    driver.maximize_window()
    yield driver
    driver.quit()


def test_upload(driver):
    driver.get('http://demo.guru99.com/test/upload/')

    dir_name = path.dirname(__file__)
    full_name = path.join(dir_name, '1.png')

    input_file = driver.find_element_by_name('uploadfile_0')
    sleep(3)
    input_file.send_keys(full_name)
    sleep(5)

    driver.find_element_by_id('submitbutton').click()


def test_upload_radical(driver):
    driver.get('https://radikal.ru/')

    dir_name = path.dirname(__file__)
    full_name = path.join(dir_name, '1.png')

    input_file = driver.find_element_by_class_name('upload1')
    sleep(3)
    input_file.send_keys(full_name)
    sleep(5)


def test_hidden_upload_element(driver):
    # Заходим в yoгtube-studio и авторизуемся
    driver.get('https://studio.youtube.com/channel/')

    element = driver.find_element_by_id('identifierId')
    element.send_keys('your_login')
    element = driver.find_element_by_xpath(
        "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qIypjc TrZEUc']")
    element.click()

    pass_element = driver.find_element_by_xpath("//div[@class='rFrNMe ze9ebf YKooDc q9Nsuf zKHdkd sdJrJc']")
    pass_element.send_keys('your_password')
    btn = driver.find_element_by_xpath(
        "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qIypjc TrZEUc']")
    btn.click()

    create_btn = driver.find_element_by_xpath("//div[@class='label style-scope ytcp-button'][text()='Создать']")
    create_btn.click()

    # Выполняем js-скрипт для доступности элемента. Далее можно работать с элементом и загружать файл
    driver.execute_script('''a = document.getElementsByName('Filedata')
                            file_input = a[0]
                            file_input.style["top"]="10px"
                            file_input.style["left"]="10px"
                            file_input.style["width"]="120px"
                            file_input.style["height"]="50px"
                            file_input.style["opacity"]="100"
                            file_input.style["overflow"]="visible"
                            file_input.style["display"]="block"
                            file_input.style["position"]="relative" 
                            '''
                          )

